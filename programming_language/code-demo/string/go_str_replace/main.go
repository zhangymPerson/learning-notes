package main

import (
	"log"
	"os"
	"strings"

	"github.com/atotto/clipboard"
	"github.com/spf13/viper"
	"github.com/urfave/cli/v2"
)

// 配置文件地址
var configFile string

// 文本内容
var content string

var contentFile string

// go run main.go -f replace.yaml -c aaaaccccccc
func main() {
	app := &cli.App{
		Name:  "replace",
		Usage: "字符串替换",
		// 两个参数 一个是 config 配置文件位置
		// 一个是 文本内容 str
		Flags: []cli.Flag{
			&cli.StringFlag{
				Name:    "config",
				Value:   "replace.yaml",
				Usage:   "配置文件位置",
				Aliases: []string{"c"},
			},
			&cli.StringFlag{
				Name:    "content",
				Value:   "",
				Usage:   "要实现替换的文本内容",
				Aliases: []string{"s"},
			},
			&cli.StringFlag{
				Name:    "file",
				Value:   "",
				Usage:   "要替换的内容所在文件位置",
				Aliases: []string{"f"},
			},
		},
		Args:   true,
		Action: replace,
	}

	if err := app.Run(os.Args); err != nil {
		log.Fatal(err)
	}
}

func replace(c *cli.Context) error {
	configFile = c.String("config")
	content = c.String("content")
	contentFile = c.String("file")
	log.Printf("configFile = [%+v]\n", configFile)
	// 获取非标志参数，即位置参数
	if content == "" {
		args := c.Args().Slice()
		content = strings.Join(args, " ")
	}
	if content == "" {
		content = getStringFromFile(contentFile)
	}
	log.Printf("原始文本 = [%+v]\n", content)
	// 读取配置文件
	config := getConfig(configFile)
	replaces := config.Replaces
	if len(replaces) > 0 {
		for _, replace := range replaces {
			content = strings.ReplaceAll(content, replace.OldText, replace.NewText)
		}
	}
	log.Printf("\n%+v\n", content)
	// 将文本写入剪贴板
	err := clipboard.WriteAll(content)
	if err != nil {
		log.Fatal("写入剪切板异常,异常信息如下:", err)
	} else {
		log.Printf("写入剪切板成功")
	}
	return nil
}

type Replace struct {
	OldText string `mapstructure:"old-text"`
	NewText string `mapstructure:"new-text"`
}

type Config struct {
	Replaces []Replace `mapstructure:"replaces"`
}

func getConfig(configFile string) *Config {
	// 设置配置文件的路径和类型
	viper.AddConfigPath("/etc")
	viper.AddConfigPath("$HOME/.config")
	viper.SetConfigFile(configFile)

	// 读取配置文件
	err := viper.ReadInConfig()
	if err != nil {
		log.Fatalf("读取配置出错，配置文件为, %s,%s", configFile, err)
	}

	var config Config
	err = viper.Unmarshal(&config)
	if err != nil {
		log.Fatalf("解析配置出错，配置文件为, %s", err)
	}
	// log.Printf("config = [%+v]\n", config)
	return &config
}

func getStringFromFile(filename string) string {
	// 读取文件中的所有文本返回
	byte, err := os.ReadFile(filename)
	if err != nil {
		log.Fatalf("读取文件出错，文件为, %s", err)
	}
	return string(byte)
}
