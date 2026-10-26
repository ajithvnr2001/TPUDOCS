---
name: setup-10-pricing
description: "Cloud TPU pricing \u2014 Official current price reference linked from TPU quota and regions documentation; use it to compare generation, zone, and consumption mode."
source_url: "https://cloud.google.com/tpu/pricing"
category: "tpu_setup_docs"
---

# Agent Skill: Cloud TPU pricing

- **Official Source**: [https://cloud.google.com/tpu/pricing](https://cloud.google.com/tpu/pricing)
- **Category**: `tpu_setup_docs`
- **Resource ID**: `setup_10_pricing`
- **When to Activate**: Official current price reference linked from TPU quota and regions documentation; use it to compare generation, zone, and consumption mode.

## Document Sections

- **Cloud TPU pricing**
  - **Regional pricing**
  - **Cloud TPU usage options**
  - **Chips vs Cores vs VMs**
  - **Estimate your cost**
  - **Take the next step**
  - **Request a custom quote**

## Complete Technical Reference

# Cloud TPU pricing
Get a custom quote[](https://cloud.google.com/contact)
Learn more about Cloud TPU[](https://cloud.google.com/tpu)
## Regional pricing
Cloud TPU pricing varies by product, deployment model & region. Charges for Cloud TPU accrue while a TPU node is in a READY state. Customers receive a bill at the end of each billing cycle that lists usage and charges for that billing cycle. Prices displayed here are **per chip-hour in USD**.
HourlyHourly
MonthlyMonthly  
|  Cloud TPU Version (per chip-hour)  | Region  | Location  |  On Demand (USD) (per hour or per month)  | DWS Flex-start price (USD)  | DWS Calendar Mode price (USD)  |  1-year Commitment (USD) (per hour or per month)  |  3-year Commitment (USD) (per hour or per month)  |  
| --- | --- | --- | --- | --- | --- | --- | --- |  
| Ironwood  | us-central1  | Iowa  | $12.00  | $6.00 / 1 hour  | $8.40 / 1 hour  | $8.40  | $5.40  |  
| europe-west2  | London  | $13.20  | $6.00 / 1 hour  | $8.40 / 1 hour  | $9.24  | $5.94  |  
| Trillium  | us-east1  | South Carolina  | $2.70  | $1.35 / 1 hour  | $1.89 / 1 hour  | $1.89  | $1.22  |  
| us-east5  | Ohio  | $2.70  | $1.35 / 1 hour  | $1.89 / 1 hour  | $1.89  | $1.22  |  
| europe-west4  | Amsterdam  | $2.97  | $1.35 / 1 hour  | $1.89 / 1 hour  | $2.08  | $1.34  |  
| asia-northeast1  | Tokyo  | $3.24  | $1.35 / 1 hour  | $1.89 / 1 hour  | $2.27  | $1.46  |  
| TPU v5p  | us-east5  | Columbus  | $4.20  | $2.10 / 1 hour  | $2.94 / 1 hour  | $2.94  | $1.89  |  
| us-east1  | South Carolina  | $4.20  |  $2.10 / 1 hour  | $2.94 / 1 hour  | $2.94  | $1.89  |  
| TPU v5e  | us-central1  | Iowa  | $1.20  | $0.60 / 1 hour  | $0.84 / 1 hour  | $0.84  | $0.54  |  
| us-east5  | Columbus  | $1.20  | $0.60 / 1 hour  | $0.84 / 1 hour  | $0.84  | $0.54  |  
| us-south1  | Dallas  | $1.416  | $0.60 / 1 hour  | $0.84 / 1 hour  | $0.9912  | $0.6372  |  
| us-west1  | Oregon  | $1.20  | $0.60 / 1 hour  | $0.84 / 1 hour  | $0.84  | $0.54  |  
| us-west4  | Las Vegas  | $1.20  | $0.60 / 1 hour  | $0.84 / 1 hour  | $0.84  | $0.54  |  
| europe-west1  | Belgium  | $1.32132  | $0.60 / 1 hour  | $0.84 / 1 hour  | $0.924924  | $0.594594  |  
| europe-west4  | Netherlands  | $1.56  | $0.60 / 1 hour  | $0.84 / 1 hour  | $1.092  | $0.702  |  
| asia-southeast1  | Singapore  | $1.56  | $0.60 / 1 hour  | $0.84 / 1 hour  | $1.092  | $0.702  |  
| TPU v4 pod  | us-central2  | Oklahoma  | $3.22  | N/A  | N/A  | $2.0286  | $1.449  |  
| TPU v3 pod  | europe-west4  | Netherlands  | $2.00  | N/A  | N/A  | $1.26  | $0.90  |  
| TPU v3 device  | europe-west4  | Netherlands  | $2.20  | N/A  | N/A  | $1.386  | $0.99  |  
| TPU v2 pod  | us-central1  | Iowa  | $1.50  | N/A  | N/A  | $0.945  | $0.675  |  
| europe-west4  | Netherlands  | $1.50  | N/A  | N/A  | $0.945  | $0.675  |  
| TPU v2 device  | asia-east1  | Taiwan  | $1.305  | N/A  | N/A  | $0.82215  | $0.58725  |  
| europe-west4  | Netherlands  | $1.2375  | N/A  | N/A  | $0.779625  | $0.556875  |  
Spot prices are dynamic and can change up to once every 30 days. For more information, see the [Spot VMs](https://cloud.google.com/compute/docs/instances/spot#pricing) documentation.
## Cloud TPU usage options
| Type  | Billing  | Best fit for:  |  
| --- | --- | --- |  
| 3-year commitment (3Y CUD)  | Monthly, based on reserved quota  | ML users who need a more consistent access to 512+ cores of capacity compared to On Demand or Spot options  |  
| 1-year commitment (1Y CUD)  | Monthly, based on reserved quota  | ML users who need a more consistent access to 32-512 cores of capacity compared to On Demand or Spot options  |  
| On Demand  | Hourly, based on actual usage  | ML users who want to run some short-term experiments or benchmarks  |  
| Spot/Preemptible  | Hourly, based on actual usage  | ML users who want to run batch / fault-tolerant workloads  |  
## Chips vs Cores vs VMs
Pricing shown above is per chip-hour. A single TPU Virtual Machine (VM) can have multiple chips and at least 2 cores. Billing in the Google Cloud console is displayed in VM-hours (for example, the on-demand price for a single Cloud TPU v4 host, which includes four TPU v4 chips and one VM, is displayed as $12.88 per hour). Usage data in the Google Cloud console is also measured in VM-hours.
## Estimate your cost
Estimate the cost of using Cloud TPU with the [Compute Engine pricing calculator](https://cloud.google.com/products/calculator), choose “Cloud TPU” on the top bar.
## Take the next step
  * [Contact our sales team](https://cloud.google.com/contact?direct=true) to purchase quota and/or learn more about Cloud TPU.
  * Look [inside a Google Cloud TPU Data Center](https://www.youtube.com/watch?v=FsxthdQ_sL4).
  * Introducing [the next evolution of container platforms](https://cloud.google.com/blog/products/containers-kubernetes/whats-new-with-gke-at-google-cloud-next) with TPU support in GKE.
  * Read the Cloud TPU [quota policy](https://cloud.google.com/tpu/docs/quota) page to learn how to request quota for different TPU types.
  * Check the [regions and zones](https://cloud.google.com/tpu/docs/regions-zones) in which Cloud TPU is available.
  * Check the [release notes](https://cloud.google.com/tpu/docs/release-notes) for future updates on pricing.
  * Read the [Cloud TPU documentation](https://cloud.google.com/tpu/docs).
  * Get started with [Cloud TPU](https://cloud.google.com/tpu/docs/quick-starts).
  * Learn about [Cloud TPU solutions and use cases](https://cloud.google.com/architecture?text=Cloud%20TPU).


## Request a custom quote
With Google Cloud's pay-as-you-go pricing, you only pay for the services you use. Connect with our sales team to get a custom quote for your organization.
Contact sales[](https://cloud.google.com/contact?direct=true)
