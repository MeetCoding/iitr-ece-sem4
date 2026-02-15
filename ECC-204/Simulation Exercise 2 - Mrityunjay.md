![[Pasted image 20260215225210.png]]

AC analysis:

![[Pasted image 20260215225801.png]]

Gain analysis with varying frequency:

![[Pasted image 20260215225254.png]]

To fulfill the design requirements for the two-stage amplifier, the following derivation outlines the necessary component sizing and biasing strategies.
### 1. Initial Design Parameters
The design is grounded in the following fixed constraints and assumed process characteristics for 180nm technology:

- **Supply ($V_{DD}$):** $1.8\text{V}$
    
- **Physical Dimensions:** $L = 1\mu\text{m}$ for all MOSFETs
    
- **Assumed Process Values:** $V_{to} = 0.5\text{V}$, $K_p (\mu_n C_{ox}) = 400 \mu\text{A/V}^2$, and $\lambda = 0.1\text{V}^{-1}$
    
- **Operating Targets:** $V_{OV} = 0.15\text{V}$ and $R_L = 50\Omega$
    
 
### 2. Primary Gain Stage: Common-Gate Topology

The first stage utilizes $M_2$ as the active amplifier and $M_1$ as a current source load.

#### **A. Input Impedance and Transconductance**

Given the requirement for a $50\Omega$ input resistance ($R_{in}$):

$$g_{m2} = \frac{1}{R_{in}} = \frac{1}{50\Omega} = \mathbf{20\text{mS}}$$

#### **B. Determining $R_D$ for Target Gain**

To achieve the specified voltage gain of 10 for the CG stage:

$$R_D = \frac{A_{v1}}{g_{m2}} = \frac{10}{0.02\text{A/V}} = \mathbf{500\Omega}$$

#### **C. Bias Current and DC Levels**

- **Operating Current:** $I_{D1,2} = \frac{g_{m2} \cdot V_{OV}}{2} = \frac{0.02 \cdot 0.15}{2} = \mathbf{1.5\text{mA}}$
    
- **Drain Potential ($V_{D2}$):** $V_{DD} - (I_{D2} \cdot R_D) = 1.8\text{V} - 0.75\text{V} = \mathbf{1.05\text{V}}$
    
- **Gate Bias ($V_{B1}$):** With $V_{GS} = 0.65\text{V}$ and a chosen source potential of $0.25\text{V}$ to ensure $M_1$ saturation:
    
    $$V_{B1} = V_{S2} + V_{GS2} = 0.25\text{V} + 0.65\text{V} = \mathbf{0.9\text{V}}$$
    
- **Current Source Bias ($V_{B0}$):** $V_{GS1} = \mathbf{0.65\text{V}}$
    

### 3. Buffer Stage: Common-Drain Configuration

The second stage provides current drive via $M_3$, with $M_4$ acting as the tail current source.

#### **A. Transconductance for Gain Matching**

For a CD gain of 0.9 driving a $50\Omega$ load:

$$0.9 = \frac{g_{m3} \cdot 50}{1 + g_{m3} \cdot 50} \implies \mathbf{g_{m3} = 180\text{mS}}$$

#### **B. Power and Output Biasing**

- **Bias Current:** $I_{D3,4} = \frac{0.18 \cdot 0.15}{2} = \mathbf{13.5\text{mA}}$
    
- **Quiescent Output ($V_{S3}$):** Specified $V_{G3} = 1.3\text{V}$. Thus, $V_{S3} = 1.3\text{V} - 0.65\text{V} = \mathbf{0.65\text{V}}$.
    

### 4. Transistor Geometry Summary

Device widths ($W$) are calculated using the square-law saturation model ($I_D = \frac{1}{2} K_p \frac{W}{L} V_{OV}^2$):

+1

|**Device**|**ID​ (mA)**|**gm​ (mS)**|**W/L Ratio**|**Width (L=1μm)**|
|---|---|---|---|---|
|**$M_1, M_2$**|1.5|20|333.3|**$333.3\mu\text{m}$**|
|**$M_3, M_4$**|13.5|180|3000|**$3000\mu\text{m}$**|

### 5. Final Constraints and Performance

- **Saturation Verification:** All devices maintain $V_{DS} > V_{OV}$ ($0.15\text{V}$), ensuring high-gain operation.
    
- **AC Coupling:** To accommodate the $1\text{kHz}$ minimum frequency , capacitors must exceed $3.18\mu\text{F}$. We select **$100\mu\text{F}$** for flat frequency response down to $10\text{Hz}$.
    
- **Calculated Total Gain:** $A_{total} = 10 \times 0.9 = \mathbf{9 \text{ (19.1 dB)}}$