# 分布式系统

- 分布式架构

  [分布式架构-百度百科](https://baike.baidu.com/item/分布式架构/9618693)

- 发展

  ![系统架构进化图](../Picture/%E7%B3%BB%E7%BB%9F%E6%9E%B6%E6%9E%84%E5%8F%91%E5%B1%95%E5%9B%BE.png)

- 分布式理论

  CAP、BASE

- CAP 理论

  C(consistency) 一致性

        所有分区节点数据时刻保持同步

  A(Availability)可用性

        每个请求都能接收到一个响应，无论响应的成功或者失败

  P(Partition-tolerance) 分区容错性

        系统应该持续提供服务，即时系统内部（某个 节点分区）有消息丢失。比如交换机失败、网址网络被分 成几个子网，形成脑裂；服务器发生网络延迟或死机，导 致某些server与集群中的其他机器失去联系

  理论:一致性（Consistency）、可用性（Availability）、分区容错 （Partition-tolerance）三者无法在分布式系统中同时被满 足，并且最多只能满足两个！

  总结一下：CAP 并不是一个普适性原理和指导思想，它仅 适用于原子读写的 NoSql 场景中，并不适用于数据库系统。

- BASE 理论

  BASE 全称 是 Basically available,soft-state,Eventually Consistent. 系统基本可用、软状态、数据最终一致性。相对于 CAP 来 说，它大大降低了我们对系统的要求。

  Basically available（基本可用），在分布式系统出现不可预 知的故障时，允许瞬时部分可用性

  soft-state（软状态）. 表示系统中的数据存在中间状态，并 且这个中间状态的存在不会影响系统的整体可用性，也就 是表示系统允许在不同节点的数据副本之间进行数据同步 过程中存在延时； 比如订单状态，有一个待支付、支付中、 支付成功、支付失败， 那么支付中就是一个中间状态，这 个中间状态在支付成功以后，在支付表中的状态同步给订 单状态之前，中间会存在一个时间内的不一致。

  Eventually consistent（数据的最终一致性），表示的是所有 数据副本在一段时间的同步后最终都能达到一个一直的状 态，因此最终一致性的本质是要保证数据最终达到一直， 而不需要实时保证系统数据的强一致

  BASE 理论的核心思想是：即使无法做到强一致性，但每个 应用都可以根据自身业务特点，采用适当的方式来使系统 达到最终一致性
