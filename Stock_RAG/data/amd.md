# AMD (Advanced Micro Devices)

AMD is the primary alternative GPU vendor to NVIDIA in the AI accelerator market.

## AI GPU Position
- MI300X is AMD's flagship AI accelerator
- Competitive with H100 for inference workloads; lower cost per token
- AI GPU revenue: $5B (2024), targeting $7.5B+ (2025)

## MI300X Advantages
- 192GB HBM3 memory capacity vs H100's 80GB — advantage for large model inference
- Lower price point than H100; attractive for cost-sensitive buyers
- Used by Microsoft Azure, Meta for inference deployments

## Software Gap
- ROCm (AMD's CUDA alternative) is improving but ~2–3 years behind CUDA
- Most AI frameworks (PyTorch, JAX) work on ROCm but with friction
- Developer mindshare remains strongly CUDA-first

## Supply Chain
- Manufactured at TSMC N5/N4 nodes
- HBM sourced from Micron (differentiating from NVIDIA's SK Hynix dependency)
- Less packaging constraint than NVIDIA due to different HBM stacking approach

## Financial Highlights
- Total Revenue: ~$25B (2024)
- Data Center Revenue: ~$12B (2024, includes CPUs + GPUs)
- Gross Margin: ~53%
- Forward P/E: ~40x

## Opportunity
- Enterprises seeking NVIDIA supply alternatives
- Open-source model community (LLaMA, Mistral) increasingly ROCm-compatible
- Custom ASIC customers potentially reverting to GPUs if ASIC timelines slip
