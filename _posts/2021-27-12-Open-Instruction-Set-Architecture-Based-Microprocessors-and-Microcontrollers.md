---
layout: post
title: Open Instruction Set Architecture Based Microprocessors and Microcontrollers
date:  2021-12-27 11:27:00 +0900
categories: [Open Hardware]
tags: [RISCV, Microprocessors, Microcontrollers]
---

Open Instruction Set Architecture Based Microprocessors and Microcontrollers

**RISC-V** is an interesting architecture that will be a fit for open hardware enthusiasts who are working with various open hardware development boards. **RISC stands for “reduced instruction set computer”**, it's an open-source hardware architecture thats sets it a side from most others. Originally developed at Parallel Computing Laboratory, UC Berkely. it has no proprietary licensing. so anybody can build RISC-V microprocessors however they want and it increasingly popular, especially for embedded system on chip.

If we see designers are under constant pressure to innoate yet to keep their intellectual property(IP) secret. This RISC-V open source hardware instruction set architecture(ISA) may interesting for hardware designers, researchers, and students to understanding of basic concepts and theories of computer architecture by making their own RISC-V CPU core.

So, whats's unique about RISC-V base microcontroller developmentboards and RISC-V core which is in it? 
We know the core, we know RISC-V, we know the software, we know the hardware, we know the chip layout - **Full Control - That's the beauty of hardware** that designed with RISC-V, open instruction set architecture. We are in full control of everything including it's security.

This Architecture is fairly new, and there is only one microcontroller widely available for RISC-V right now. it's SiFive freedom E310-G002. here are a collection of available physical hardware development boards based on RISC-V architecture.

- [BeagleV™ ](https://beagleboard.org/static/beagleV/beagleV.html)
- [SiFive HiFive1 Rev B](https://www.sifive.com/boards/hifive1-rev-b)
- [SiFive HiFive Unmatched](https://www.sifive.com/boards/hifive-unmatched)
- [LoFive RISC-V](https://groupgets.com/manufacturers/qwerty-embedded-design/products/lofive-risc-v)
- [GAPduino Development Board](https://gitee.com/bluetrum/AB32VG1_DOC/tree/master)
- [SparkFun RED-V RedBoard](https://www.sparkfun.com/products/15594)

Getting started with RISC-V processors is a little bit different than standard microcontroller ecosystem. Setting up RISC-V tool chain and programming development boards is not much more difficult than any other standard microcontroller. But RISC-V is intriguing, it doesn't have the rich ecosystem that many existing microcontroller platform have. So, if we choose to go in the RISC-V path we may find fewer choices and resources to leverage. Instead of compromising on end application, resources let's contribute to tooling, hardware development practices by working with RISC-V community.

Anyway, let's be realistic this new open instruction set architecture is not the only thing needed to make the open hardware revolution happen, it's an enabler and a solution to lower the barriers to innovate(no licence but sharing design instead). Obviously, not everyone is able to design an entire CPU from scratch, we can bring only what we need or even just use new capabilities provided by the community, exactly the same way we do with free software, from kernel to languages (Rust community as a modern example).

#### References:
- [A New Golden Age for Computer Architecture By John L. Hennessy, David A. Patterson](https://cacm.acm.org/magazines/2019/2/234352-a-new-golden-age-for-computer-architecture/fulltext) 
- [https://www.acm.org/hennessy-patterson-turing-lecture](https://www.acm.org/hennessy-patterson-turing-lecture)
- [https://github.com/riscv/riscv-isa-manual](https://github.com/riscv/riscv-isa-manual)
- [https://riscv.org/](https://riscv.org/)
