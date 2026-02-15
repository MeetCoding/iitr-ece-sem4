### Design Constants and Specifications

The following parameters are established based on the assignment constraints and the requested typical values for 180nm technology:

- **Supply Voltage ($V_{DD}$):** $1.8\text{V}$
- **Threshold Voltage ($V_{to}$):** $0.5\text{V}$ (Assumed)
- **Channel Length Modulation ($\lambda$):** $0.1\text{V}^{-1}$ (Assumed)
- **Overdrive Voltage ($V_{OV}$):** $0.15\text{V}$ (Assumed)
- **Process Transconductance ($K_p = \mu_n C_{ox}$):** $400 \mu\text{A/V}^2$ (Assumed)
- **Load Resistance ($R_L$):** $50\Omega$
- **Channel Length ($L$):** $1\mu\text{m}$ for all transistors

### First Stage: Common-Gate (CG) Amplifier Design

The first stage consists of $M_2$ as the CG amplifier and $M_1$ acting as the current source.
#### Transconductance ($g_m$) and Input Resistance
The small-signal input resistance for a CG amplifier is approximately $R_{in} \approx 1/g_{m2}$. Given $R_{in} = 50\Omega$:
$$g_{m2} = \frac{1}{R_{in}} = \frac{1}{50} = \mathbf{0.02 \text{ A/V}} = 20 \text{ mS}$$
#### **B.Drain Resistance ($R_D$)

The gain of the CG stage ($A_{v1}$) is given by $g_{m2} \cdot R_D$. Given $A_{v1} = 10$:

$$R_D = \frac{A_{v1}}{g_{m2}} = \frac{10}{0.02} = \mathbf{500 \Omega}$$

#### **C. Drain Current ($I_D$)**

Using the relationship $g_m = \frac{2I_D}{V_{OV}}$:

$$I_{D1,2} = \frac{g_{m2} \cdot V_{OV}}{2} = \frac{0.02 \cdot 0.15}{2} = \mathbf{1.5 \text{ mA}}$$

#### **D. DC Voltages and Biasing ($V_{B0}, V_{B1}$)**

- **Voltage drop across $R_D$ ($V_{RD}$):**
    
    $$V_{RD} = I_{D2} \cdot R_D = 1.5\text{mA} \cdot 500\Omega = \mathbf{0.75 \text{ V}}$$
    
- **Drain voltage of $M_2$ ($V_{D2}$):**
    
    $$V_{D2} = V_{DD} - V_{RD} = 1.8\text{V} - 0.75\text{V} = \mathbf{1.05 \text{ V}}$$
    
- **Gate-Source voltage ($V_{GS2}$):**
    
    $$V_{GS2} = V_{to} + V_{OV} = 0.5\text{V} + 0.15\text{V} = 0.65\text{V}$$
    
- **Source voltage of $M_2$ ($V_{S2}$):** Assuming $M_1$ requires $V_{DS1} \geq V_{OV} = 0.15\text{V}$ to stay in saturation, we set **$V_{S2} = 0.25\text{V}$** to provide headroom.
    
- **Bias Voltages:**
    
    $$V_{B1} = V_{S2} + V_{GS2} = 0.25\text{V} + 0.65\text{V} = \mathbf{0.9 \text{ V}}$$
    
    $$V_{B0} = V_{S1} + V_{GS1} = 0\text{V} + 0.65\text{V} = \mathbf{0.65 \text{ V}}$$
    

---

### **3. Second Stage: Common-Drain (CD) Amplifier Design**

The second stage consists of $M_3$ as the CD amplifier (Source Follower) and $M_4$ as the current source.

+1

#### **A. Transconductance ($g_{m3}$)**

The gain of the CD stage is $A_{v2} = \frac{g_{m3}R_L}{1 + g_{m3}R_L}$. Given $A_{v2} = 0.9$ and $R_L = 50\Omega$:

+1

$$0.9 = \frac{g_{m3} \cdot 50}{1 + g_{m3} \cdot 50} \implies 0.9 + 45g_{m3} = 50g_{m3} \implies \mathbf{g_{m3} = 0.18 \text{ A/V}} = 180 \text{ mS}$$

#### **B. Drain Current ($I_{D3}$)**

Using the same overdrive $V_{OV} = 0.15\text{V}$:

$$I_{D3,4} = \frac{g_{m3} \cdot V_{OV}}{2} = \frac{0.18 \cdot 0.15}{2} = \mathbf{13.5 \text{ mA}}$$

#### **C. DC Voltages ($V_{S3}$)**

- The gate of $M_3$ is biased at **$1.3\text{V}$** per specifications.
    
- **Source voltage ($V_{S3}$):**
    
    $$V_{S3} = V_{G3} - V_{GS3} = 1.3\text{V} - 0.65\text{V} = \mathbf{0.65 \text{ V}}$$
    

---

### **4. Transistor Sizing ($W/L$)**

Calculated using the saturation current equation: $I_D = \frac{1}{2} K_p \frac{W}{L} V_{OV}^2$ (ignoring $\lambda$ for hand calcs).

+1

|**Transistor**|**ID​ (mA)**|**gm​ (mS)**|**Calculated W/L**|**Final W (L=1μm)**|
|---|---|---|---|---|
|**$M_1$**|$1.5$|$20$|$\frac{2 \cdot 1.5\text{m}}{400\mu \cdot 0.15^2} \approx \mathbf{333.3}$|$333.3\mu\text{m}$|
|**$M_2$**|$1.5$|$20$|$\frac{2 \cdot 1.5\text{m}}{400\mu \cdot 0.15^2} \approx \mathbf{333.3}$|$333.3\mu\text{m}$|
|**$M_3$**|$13.5$|$180$|$\frac{2 \cdot 13.5\text{m}}{400\mu \cdot 0.15^2} = \mathbf{3000}$|$3000\mu\text{m}$|
|**$M_4$**|$13.5$|$180$|$\frac{2 \cdot 13.5\text{m}}{400\mu \cdot 0.15^2} = \mathbf{3000}$|$3000\mu\text{m}$|

---

### **5. Saturation and Capacitor Constraints**

**Saturation Checks ($V_{DS} \geq V_{GS} - V_{th}$)**

- **$M_1$:** $V_{DS1} = 0.25\text{V} > 0.15\text{V}$ (**OK**)
    
- **$M_2$:** $V_{DS2} = (1.05 - 0.25) = 0.8\text{V} > 0.15\text{V}$ (**OK**)
    
- **$M_3$:** $V_{DS3} = (1.8 - 0.65) = 1.15\text{V} > 0.15\text{V}$ (**OK**)
    
- **$M_4$:** $V_{DS4} = 0.65\text{V} > 0.15\text{V}$ (**OK**)
    

#### **Coupling Capacitors ($C_1, C_2$)**

To ensure the pole frequency is below the minimum frequency of **$1\text{kHz}$**:

$$f_p = \frac{1}{2\pi RC} \ll 1000\text{Hz}$$

For $R = 50\Omega$:

+1

$$C \gg \frac{1}{2\pi \cdot 1000 \cdot 50} \approx 3.18 \mu\text{F}$$

To meet the $10\text{Hz}$ to $1\text{MHz}$ sweep requirement, use **$C_1 = C_2 = 100\mu\text{F}$**.

#### **Overall Gain**

$$A_{total} = A_{v1} \times A_{v2} = 10 \times 0.9 = \mathbf{9} \text{ (or } \approx 19.1 \text{ dB)}$$