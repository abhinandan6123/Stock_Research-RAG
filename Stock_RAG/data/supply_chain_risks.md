# AI Supply Chain Bottlenecks & Risks

The AI hardware supply chain has multiple critical chokepoints that constrain the pace of AI infrastructure deployment globally.

## Bottleneck 1: HBM Memory Shortage
- High Bandwidth Memory (HBM3/HBM3e) is essential for AI accelerators
- Only three suppliers: SK Hynix (~50%), Samsung (~30%), Micron (~20%)
- HBM production requires repurposing DRAM fabs — slow to scale
- AI demand for HBM growing at 100%+ annually; supply at ~30–40%
- Shortage expected to persist through 2025

## Bottleneck 2: Advanced Packaging
- CoWoS (Chip-on-Wafer-on-Substrate) used to bond HBM to GPU die
- TSMC controls CoWoS; capacity severely limited
- Cannot simply add capacity quickly — requires 18–24 month fab buildout
- Directly limits how many H100/H200 units NVIDIA can ship

## Bottleneck 3: Foundry Capacity
- TSMC N3/N4 nodes fully booked by Apple, NVIDIA, AMD, Qualcomm
- Samsung yield on 3nm remains below TSMC; not a viable alternative
- Intel Foundry Services lacks customers and yield credibility at advanced nodes

## Bottleneck 4: Power Infrastructure
- AI data centers require 10–50 MW per cluster
- US power grid approval process: 5–10 years for new transmission
- Hyperscalers turning to nuclear: Microsoft (Three Mile Island), Google, Amazon
- Diesel generator supply and electrical switchgear also constrained

## Bottleneck 5: Networking Equipment
- 400G/800G optical transceivers needed for GPU-to-GPU communication
- InfiniBand (NVIDIA) and Ethernet (Broadcom) compete for AI fabric
- Optical component supply (lasers, coherent modules) constrained

## Geopolitical Risks
- US export controls ban H100/H200/A100 sales to China
- China developing HuaWei Ascend 910B as domestic alternative (less capable)
- ASML EUV machines blocked from China export
- Taiwan conflict scenario: worst case for global chip supply

## Investment Implications
- Short-term: Bottlenecks = pricing power for NVIDIA, TSMC, SK Hynix
- Medium-term: Capacity additions in 2025–2026 may cause oversupply in some areas
- Long-term: Geographic diversification of supply chain (US, Japan, EU fabs)
