###
### This file was automatically generated
###

from archinfo.arch import register_arch, Endness, Register

from .common import ArchPcode


class ArchPcode_MIPS_LE_64_default(ArchPcode):
    name = 'MIPS:LE:64:default'
    pcode_arch = 'MIPS:LE:64:default'
    description = 'MIPS64 64-bit addreses, little endian, with mips16e'
    bits = 64
    ip_offset = 0x100
    sp_offset = 0xe8
    bp_offset = sp_offset
    instruction_endness = Endness.LE
    register_list = [
        Register('zero', 8, 0x0),
        Register('zero_lo', 4, 0x0),
        Register('zero_hi', 4, 0x4),
        Register('at', 8, 0x8),
        Register('at_lo', 4, 0x8),
        Register('at_hi', 4, 0xc),
        Register('v0', 8, 0x10),
        Register('v0_lo', 4, 0x10),
        Register('v0_hi', 4, 0x14),
        Register('v1', 8, 0x18),
        Register('v1_lo', 4, 0x18),
        Register('v1_hi', 4, 0x1c),
        Register('a0', 8, 0x20),
        Register('a0_lo', 4, 0x20),
        Register('a0_hi', 4, 0x24),
        Register('a1', 8, 0x28),
        Register('a1_lo', 4, 0x28),
        Register('a1_hi', 4, 0x2c),
        Register('a2', 8, 0x30),
        Register('a2_lo', 4, 0x30),
        Register('a2_hi', 4, 0x34),
        Register('a3', 8, 0x38),
        Register('a3_lo', 4, 0x38),
        Register('a3_hi', 4, 0x3c),
        Register('t0', 8, 0x40),
        Register('t0_lo', 4, 0x40),
        Register('t0_hi', 4, 0x44),
        Register('t1', 8, 0x48),
        Register('t1_lo', 4, 0x48),
        Register('t1_hi', 4, 0x4c),
        Register('t2', 8, 0x50),
        Register('t2_lo', 4, 0x50),
        Register('t2_hi', 4, 0x54),
        Register('t3', 8, 0x58),
        Register('t3_lo', 4, 0x58),
        Register('t3_hi', 4, 0x5c),
        Register('t4', 8, 0x60),
        Register('t4_lo', 4, 0x60),
        Register('t4_hi', 4, 0x64),
        Register('t5', 8, 0x68),
        Register('t5_lo', 4, 0x68),
        Register('t5_hi', 4, 0x6c),
        Register('t6', 8, 0x70),
        Register('t6_lo', 4, 0x70),
        Register('t6_hi', 4, 0x74),
        Register('t7', 8, 0x78),
        Register('t7_lo', 4, 0x78),
        Register('t7_hi', 4, 0x7c),
        Register('s0', 8, 0x80),
        Register('s0_lo', 4, 0x80),
        Register('s0_hi', 4, 0x84),
        Register('s1', 8, 0x88),
        Register('s1_lo', 4, 0x88),
        Register('s1_hi', 4, 0x8c),
        Register('s2', 8, 0x90),
        Register('s2_lo', 4, 0x90),
        Register('s2_hi', 4, 0x94),
        Register('s3', 8, 0x98),
        Register('s3_lo', 4, 0x98),
        Register('s3_hi', 4, 0x9c),
        Register('s4', 8, 0xa0),
        Register('s4_lo', 4, 0xa0),
        Register('s4_hi', 4, 0xa4),
        Register('s5', 8, 0xa8),
        Register('s5_lo', 4, 0xa8),
        Register('s5_hi', 4, 0xac),
        Register('s6', 8, 0xb0),
        Register('s6_lo', 4, 0xb0),
        Register('s6_hi', 4, 0xb4),
        Register('s7', 8, 0xb8),
        Register('s7_lo', 4, 0xb8),
        Register('s7_hi', 4, 0xbc),
        Register('t8', 8, 0xc0),
        Register('t8_lo', 4, 0xc0),
        Register('t8_hi', 4, 0xc4),
        Register('t9', 8, 0xc8),
        Register('t9_lo', 4, 0xc8),
        Register('t9_hi', 4, 0xcc),
        Register('k0', 8, 0xd0),
        Register('k0_lo', 4, 0xd0),
        Register('k0_hi', 4, 0xd4),
        Register('k1', 8, 0xd8),
        Register('k1_lo', 4, 0xd8),
        Register('k1_hi', 4, 0xdc),
        Register('gp', 8, 0xe0),
        Register('gp_lo', 4, 0xe0),
        Register('gp_hi', 4, 0xe4),
        Register('sp', 8, 0xe8),
        Register('sp_lo', 4, 0xe8),
        Register('sp_hi', 4, 0xec),
        Register('s8', 8, 0xf0),
        Register('s8_lo', 4, 0xf0),
        Register('s8_hi', 4, 0xf4),
        Register('ra', 8, 0xf8),
        Register('ra_lo', 4, 0xf8),
        Register('ra_hi', 4, 0xfc),
        Register('pc', 8, 0x100, alias_names=('ip',)),
        Register('pc_lo', 4, 0x100),
        Register('pc_hi', 4, 0x104),
        Register('f0', 8, 0x1000),
        Register('f1', 8, 0x1008),
        Register('f2', 8, 0x1010),
        Register('f3', 8, 0x1018),
        Register('f4', 8, 0x1020),
        Register('f5', 8, 0x1028),
        Register('f6', 8, 0x1030),
        Register('f7', 8, 0x1038),
        Register('f8', 8, 0x1040),
        Register('f9', 8, 0x1048),
        Register('f10', 8, 0x1050),
        Register('f11', 8, 0x1058),
        Register('f12', 8, 0x1060),
        Register('f13', 8, 0x1068),
        Register('f14', 8, 0x1070),
        Register('f15', 8, 0x1078),
        Register('f16', 8, 0x1080),
        Register('f17', 8, 0x1088),
        Register('f18', 8, 0x1090),
        Register('f19', 8, 0x1098),
        Register('f20', 8, 0x10a0),
        Register('f21', 8, 0x10a8),
        Register('f22', 8, 0x10b0),
        Register('f23', 8, 0x10b8),
        Register('f24', 8, 0x10c0),
        Register('f25', 8, 0x10c8),
        Register('f26', 8, 0x10d0),
        Register('f27', 8, 0x10d8),
        Register('f28', 8, 0x10e0),
        Register('f29', 8, 0x10e8),
        Register('f30', 8, 0x10f0),
        Register('f31', 8, 0x10f8),
        Register('fir', 4, 0x1200),
        Register('fccr', 4, 0x1204),
        Register('fexr', 4, 0x1208),
        Register('fenr', 4, 0x120c),
        Register('fcsr', 4, 0x1210),
        Register('index', 8, 0x2000),
        Register('random', 8, 0x2008),
        Register('entrylo0', 8, 0x2010),
        Register('entrylo1', 8, 0x2018),
        Register('context', 8, 0x2020),
        Register('pagemask', 8, 0x2028),
        Register('wired', 8, 0x2030),
        Register('hwrena', 8, 0x2038),
        Register('badvaddr', 8, 0x2040),
        Register('count', 8, 0x2048),
        Register('entryhi', 8, 0x2050),
        Register('compare', 8, 0x2058),
        Register('status', 8, 0x2060),
        Register('cause', 8, 0x2068),
        Register('epc', 8, 0x2070),
        Register('prid', 8, 0x2078),
        Register('config', 8, 0x2080),
        Register('lladdr', 8, 0x2088),
        Register('watchlo', 8, 0x2090),
        Register('watchhi', 8, 0x2098),
        Register('xcontext', 8, 0x20a0),
        Register('cop0_reg21', 8, 0x20a8),
        Register('cop0_reg22', 8, 0x20b0),
        Register('debug', 8, 0x20b8),
        Register('depc', 8, 0x20c0),
        Register('perfcnt', 8, 0x20c8),
        Register('errctl', 8, 0x20d0),
        Register('cacheerr', 8, 0x20d8),
        Register('taglo', 8, 0x20e0),
        Register('taghi', 8, 0x20e8),
        Register('errorepc', 8, 0x20f0),
        Register('desave', 8, 0x20f8),
        Register('mvpcontrol', 8, 0x2100),
        Register('vpecontrol', 8, 0x2108),
        Register('tcstatus', 8, 0x2110),
        Register('cop0_reg3.1', 8, 0x2118),
        Register('contextconfig', 8, 0x2120),
        Register('pagegrain', 8, 0x2128),
        Register('srsconf0', 8, 0x2130),
        Register('cop0_reg7.1', 8, 0x2138),
        Register('cop0_reg8.1', 8, 0x2140),
        Register('cop0_reg9.1', 8, 0x2148),
        Register('cop0_reg10.1', 8, 0x2150),
        Register('cop0_reg11.1', 8, 0x2158),
        Register('intctl', 8, 0x2160),
        Register('cop0_reg13.1', 8, 0x2168),
        Register('cop0_reg14.1', 8, 0x2170),
        Register('ebase', 8, 0x2178),
        Register('config1', 8, 0x2180),
        Register('cop0_reg17.1', 8, 0x2188),
        Register('watchlo.1', 8, 0x2190),
        Register('watchhi.1', 8, 0x2198),
        Register('cop0_reg20.1', 8, 0x21a0),
        Register('cop0_reg21.1', 8, 0x21a8),
        Register('cop0_reg22.1', 8, 0x21b0),
        Register('tracecontrol', 8, 0x21b8),
        Register('cop0_reg24.1', 8, 0x21c0),
        Register('perfcnt.1', 8, 0x21c8),
        Register('cop0_reg26.1', 8, 0x21d0),
        Register('cacheerr.1', 8, 0x21d8),
        Register('datalo.1', 8, 0x21e0),
        Register('datahi.1', 8, 0x21e8),
        Register('cop0_reg30.1', 8, 0x21f0),
        Register('cop0_reg31.1', 8, 0x21f8),
        Register('mvpconf0', 8, 0x2200),
        Register('vpeconf0', 8, 0x2208),
        Register('tcbind', 8, 0x2210),
        Register('cop0_reg3.2', 8, 0x2218),
        Register('cop0_reg4.2', 8, 0x2220),
        Register('cop0_reg5.2', 8, 0x2228),
        Register('srsconf1', 8, 0x2230),
        Register('cop0_reg7.2', 8, 0x2238),
        Register('cop0_reg8.2', 8, 0x2240),
        Register('cop0_reg9.2', 8, 0x2248),
        Register('cop0_reg10.2', 8, 0x2250),
        Register('cop0_reg11.2', 8, 0x2258),
        Register('srsctl', 8, 0x2260),
        Register('cop0_reg13.2', 8, 0x2268),
        Register('cop0_reg14.2', 8, 0x2270),
        Register('cop0_reg15.2', 8, 0x2278),
        Register('config2', 8, 0x2280),
        Register('cop0_reg17.2', 8, 0x2288),
        Register('watchlo.2', 8, 0x2290),
        Register('watchhi.2', 8, 0x2298),
        Register('cop0_reg20.2', 8, 0x22a0),
        Register('cop0_reg21.2', 8, 0x22a8),
        Register('cop0_reg22.2', 8, 0x22b0),
        Register('tracecontrol2', 8, 0x22b8),
        Register('cop0_reg24.2', 8, 0x22c0),
        Register('perfcnt.2', 8, 0x22c8),
        Register('cop0_reg26.2', 8, 0x22d0),
        Register('cacheerr.2', 8, 0x22d8),
        Register('taglo.2', 8, 0x22e0),
        Register('taghi.2', 8, 0x22e8),
        Register('cop0_reg30.2', 8, 0x22f0),
        Register('cop0_reg31.2', 8, 0x22f8),
        Register('mvpconf1', 8, 0x2300),
        Register('vpeconf1', 8, 0x2308),
        Register('tcrestart', 8, 0x2310),
        Register('cop0_reg3.3', 8, 0x2318),
        Register('cop0_reg4.3', 8, 0x2320),
        Register('cop0_reg5.3', 8, 0x2328),
        Register('srsconf2', 8, 0x2330),
        Register('cop0_reg7.3', 8, 0x2338),
        Register('cop0_reg8.3', 8, 0x2340),
        Register('cop0_reg9.3', 8, 0x2348),
        Register('cop0_reg10.3', 8, 0x2350),
        Register('cop0_reg11.3', 8, 0x2358),
        Register('srsmap', 8, 0x2360),
        Register('cop0_reg13.3', 8, 0x2368),
        Register('cop0_reg14.3', 8, 0x2370),
        Register('cop0_reg15.3', 8, 0x2378),
        Register('config3', 8, 0x2380),
        Register('cop0_reg17.3', 8, 0x2388),
        Register('watchlo.3', 8, 0x2390),
        Register('watchhi.3', 8, 0x2398),
        Register('cop0_reg20.3', 8, 0x23a0),
        Register('cop0_reg21.3', 8, 0x23a8),
        Register('cop0_reg22.3', 8, 0x23b0),
        Register('usertracedata', 8, 0x23b8),
        Register('cop0_reg24.3', 8, 0x23c0),
        Register('perfcnt.3', 8, 0x23c8),
        Register('cop0_reg26.3', 8, 0x23d0),
        Register('cacheerr.3', 8, 0x23d8),
        Register('datalo.3', 8, 0x23e0),
        Register('datahi.3', 8, 0x23e8),
        Register('cop0_reg30.3', 8, 0x23f0),
        Register('cop0_reg31.3', 8, 0x23f8),
        Register('cop0_reg0.4', 8, 0x2400),
        Register('yqmask', 8, 0x2408),
        Register('tchalt', 8, 0x2410),
        Register('cop0_reg3.4', 8, 0x2418),
        Register('cop0_reg4.4', 8, 0x2420),
        Register('cop0_reg5.4', 8, 0x2428),
        Register('srsconf3', 8, 0x2430),
        Register('cop0_reg7.4', 8, 0x2438),
        Register('cop0_reg8.4', 8, 0x2440),
        Register('cop0_reg9.4', 8, 0x2448),
        Register('cop0_reg10.4', 8, 0x2450),
        Register('cop0_reg11.4', 8, 0x2458),
        Register('cop0_reg12.4', 8, 0x2460),
        Register('cop0_reg13.4', 8, 0x2468),
        Register('cop0_reg14.4', 8, 0x2470),
        Register('cop0_reg15.4', 8, 0x2478),
        Register('cop0_reg16.4', 8, 0x2480),
        Register('cop0_reg17.4', 8, 0x2488),
        Register('watchlo.4', 8, 0x2490),
        Register('watchhi.4', 8, 0x2498),
        Register('cop0_reg20.4', 8, 0x24a0),
        Register('cop0_reg21.4', 8, 0x24a8),
        Register('cop0_reg22.4', 8, 0x24b0),
        Register('tracebpc', 8, 0x24b8),
        Register('cop0_reg24.4', 8, 0x24c0),
        Register('perfcnt.4', 8, 0x24c8),
        Register('cop0_reg26.4', 8, 0x24d0),
        Register('cacheerr.4', 8, 0x24d8),
        Register('taglo.4', 8, 0x24e0),
        Register('taghi.4', 8, 0x24e8),
        Register('cop0_reg30.4', 8, 0x24f0),
        Register('cop0_reg31.4', 8, 0x24f8),
        Register('cop0_reg0.5', 8, 0x2500),
        Register('vpeschedule', 8, 0x2508),
        Register('tccontext', 8, 0x2510),
        Register('cop0_reg3.5', 8, 0x2518),
        Register('cop0_reg4.5', 8, 0x2520),
        Register('cop0_reg5.5', 8, 0x2528),
        Register('srsconf4', 8, 0x2530),
        Register('cop0_reg7.5', 8, 0x2538),
        Register('cop0_reg8.5', 8, 0x2540),
        Register('cop0_reg9.5', 8, 0x2548),
        Register('cop0_reg10.5', 8, 0x2550),
        Register('cop0_reg11.5', 8, 0x2558),
        Register('cop0_reg12.5', 8, 0x2560),
        Register('cop0_reg13.5', 8, 0x2568),
        Register('cop0_reg14.5', 8, 0x2570),
        Register('cop0_reg15.5', 8, 0x2578),
        Register('cop0_reg16.5', 8, 0x2580),
        Register('cop0_reg17.5', 8, 0x2588),
        Register('watchlo.5', 8, 0x2590),
        Register('watchhi.5', 8, 0x2598),
        Register('cop0_reg20.5', 8, 0x25a0),
        Register('cop0_reg21.5', 8, 0x25a8),
        Register('cop0_reg22.5', 8, 0x25b0),
        Register('cop0_reg23.5', 8, 0x25b8),
        Register('cop0_reg24.5', 8, 0x25c0),
        Register('perfcnt.5', 8, 0x25c8),
        Register('cop0_reg26.5', 8, 0x25d0),
        Register('cacheerr.5', 8, 0x25d8),
        Register('datalo.5', 8, 0x25e0),
        Register('datahi.5', 8, 0x25e8),
        Register('cop0_reg30.5', 8, 0x25f0),
        Register('cop0_reg31.5', 8, 0x25f8),
        Register('cop0_reg0.6', 8, 0x2600),
        Register('vpeschefback', 8, 0x2608),
        Register('tcschedule', 8, 0x2610),
        Register('cop0_reg3.6', 8, 0x2618),
        Register('cop0_reg4.6', 8, 0x2620),
        Register('cop0_reg5.6', 8, 0x2628),
        Register('cop0_reg6.6', 8, 0x2630),
        Register('cop0_reg7.6', 8, 0x2638),
        Register('cop0_reg8.6', 8, 0x2640),
        Register('cop0_reg9.6', 8, 0x2648),
        Register('cop0_reg10.6', 8, 0x2650),
        Register('cop0_reg11.6', 8, 0x2658),
        Register('cop0_reg12.6', 8, 0x2660),
        Register('cop0_reg13.6', 8, 0x2668),
        Register('cop0_reg14.6', 8, 0x2670),
        Register('cop0_reg15.6', 8, 0x2678),
        Register('cop0_reg16.6', 8, 0x2680),
        Register('cop0_reg17.6', 8, 0x2688),
        Register('watchlo.6', 8, 0x2690),
        Register('watchhi.6', 8, 0x2698),
        Register('cop0_reg20.6', 8, 0x26a0),
        Register('cop0_reg21.6', 8, 0x26a8),
        Register('cop0_reg22.6', 8, 0x26b0),
        Register('cop0_reg23.6', 8, 0x26b8),
        Register('cop0_reg24.6', 8, 0x26c0),
        Register('perfcnt.6', 8, 0x26c8),
        Register('cop0_reg26.6', 8, 0x26d0),
        Register('cacheerr.6', 8, 0x26d8),
        Register('taglo.6', 8, 0x26e0),
        Register('taghi.6', 8, 0x26e8),
        Register('cop0_reg30.6', 8, 0x26f0),
        Register('cop0_reg31.6', 8, 0x26f8),
        Register('cop0_reg0.7', 8, 0x2700),
        Register('vpeopt', 8, 0x2708),
        Register('tcschefback', 8, 0x2710),
        Register('cop0_reg3.7', 8, 0x2718),
        Register('cop0_reg4.7', 8, 0x2720),
        Register('cop0_reg5.7', 8, 0x2728),
        Register('cop0_reg6.7', 8, 0x2730),
        Register('cop0_reg7.7', 8, 0x2738),
        Register('cop0_reg8.7', 8, 0x2740),
        Register('cop0_reg9.7', 8, 0x2748),
        Register('cop0_reg10.7', 8, 0x2750),
        Register('cop0_reg11.7', 8, 0x2758),
        Register('cop0_reg12.7', 8, 0x2760),
        Register('cop0_reg13.7', 8, 0x2768),
        Register('cop0_reg14.7', 8, 0x2770),
        Register('cop0_reg15.7', 8, 0x2778),
        Register('cop0_reg16.7', 8, 0x2780),
        Register('cop0_reg17.7', 8, 0x2788),
        Register('watchlo.7', 8, 0x2790),
        Register('watchhi.7', 8, 0x2798),
        Register('cop0_reg20.7', 8, 0x27a0),
        Register('cop0_reg21.7', 8, 0x27a8),
        Register('cop0_reg22.7', 8, 0x27b0),
        Register('cop0_reg23.7', 8, 0x27b8),
        Register('cop0_reg24.7', 8, 0x27c0),
        Register('perfcnt.7', 8, 0x27c8),
        Register('cop0_reg26.7', 8, 0x27d0),
        Register('cacheerr.7', 8, 0x27d8),
        Register('datalo.7', 8, 0x27e0),
        Register('datahi.7', 8, 0x27e8),
        Register('cop0_reg30.7', 8, 0x27f0),
        Register('cop0_reg31.7', 8, 0x27f8),
        Register('hi', 8, 0x3000),
        Register('lo', 8, 0x3008),
        Register('hi1', 8, 0x3010),
        Register('lo1', 8, 0x3018),
        Register('hi2', 8, 0x3020),
        Register('lo2', 8, 0x3028),
        Register('hi3', 8, 0x3030),
        Register('lo3', 8, 0x3038),
        Register('tsp', 8, 0x3040),
        Register('isamodeswitch', 1, 0x3f00),
        Register('contextreg', 4, 0x4000)
    ]

register_arch(['mips:le:64:default'], 64, Endness.LE, ArchPcode_MIPS_LE_64_default)
