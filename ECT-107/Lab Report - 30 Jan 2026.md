***Meet Shah, 24116051***
# How EEG (Electroencephalography) Works?
 The brain is essentially neutral in charge, but individual neurons are charged and the neutrality is balanced by a equal and opposite charge on another neuron (formation of dipole).
 
 Pyramidal neurons are a cluster of neurons arranged parallel to each other and perpendicular to the scalp (near the scalp surface). The cluster of pyramidal neurons together gets positively or negatively charged.
 Charge due to individual neurons is too small to be detected, but the cluster of pyramidal neurons creates a significant measurable amount of charge.

We can connect electrodes to any two distant points on the scalp and study the potential difference between the two points to understand the brain activity.
In EEG, several such electrodes are connected and the potential difference can be measured with either a common reference electrode (Referential Montage) or can be measured between adjacent electrodes (Bipolar Montage).

In modern digital systems, we often use Common Average Reference (CAR), in which average of all electrodes on the head and use that calculated average as the reference for each individual electrode.

# Types of EEG Setup
EEG Systems can be "wet", meaning a conductive paste or gel $(AgCl)$ is applied on the scalp and then the electrodes are placed which creates a low-impedance chemical bridge.
In "dry" EEG Systems, spiky electrodes which poke through the hair are placed which have high impedance, so built-in amplifiers are used to amplifier the small signal.
The EEG data is sampled at a specific frequency, usually $250Hz$.

To navigate the head and decide location of electrodes, the International 10-20 System is used:
### The Letters (Lobe/Region)
- **$Fp$**: Frontal Pole (very front, just above the eyebrows)
- **$F$**: Frontal Lobe (executive function, logic)
- **$C$**: Central (the "midline"—note there is no "central lobe," this just marks the center)
- **$T$**: Temporal Lobe (auditory, memory)
- **$P$**: Parietal Lobe (sensory integration)
- **$O$**: Occipital Lobe (vision processing)
### The Numbers (Hemisphere & Distance)
- **Odd Numbers (1, 3, 5, 7)**: Left side of the brain.
- **Even Numbers (2, 4, 6, 8)**: Right side of the brain.
- **'z' (Zero)**: Midline electrodes (e.g., $Fz, Cz, Pz$).
- **Larger Numbers**: Farther away from the center. (e.g., $C3$ is near the middle; $T7$ is farther out by the ear).

![[Pasted image 20260129083020.png]]

# The EEG Spectrum
Doing the frequency domain analysis of these brain signals, we can classify the signals into following categories:

| **Band**             | **Frequency** | **Mental State**                                       |
| -------------------- | ------------- | ------------------------------------------------------ |
| **Delta ($\delta$)** | $0.5 - 4$ Hz  | Deep, dreamless sleep.                                 |
| **Theta ($\theta$)** | $4 - 8$ Hz    | Drowsiness, meditation, light sleep, or "flow" states. |
| **Alpha ($\alpha$)** | $8 - 13$ Hz   | Relaxed, eyes closed, calm wakefulness.                |
| **Beta ($\beta$)**   | $13 - 30$ Hz  | Active thinking, focus, alertness, or anxiety.         |
| **Gamma ($\gamma$)** | $> 30$ Hz     | High-level information processing, problem solving.    |
Note that Delta is significant only in deep sleep while Gamma is significant only during very high cognitive load. So in the EEG of an awake person, the most significant signals are Theta, Alpha and Beta.

| **Band**             | **Typical Amplitude** | **High Amplitude Condition**                                                    | **Low Amplitude Condition**                                                              |
| -------------------- | --------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Delta ($\delta$)** | $20 - 200 \mu V$      | **Deep Sleep (Stage N3):** The highest "natural" voltages in the brain.         | **Wakefulness:** Usually almost non-existent in healthy, alert adults.                   |
| **Theta ($\theta$)** | $10 - 50 \mu V$       | **Drowsiness / Hypnagogia:** Transitions into sleep or deep "Zen" meditation.   | **High Alertness:** When you are acutely focused on an external threat or fast task.     |
| **Alpha ($\alpha$)** | $20 - 100 \mu V$      | **Eyes Closed / Relaxation:** Best seen at the Occipital ($O1, O2$) electrodes. | **Eyes Open / Mental Math:** This is called "Alpha Block" or Desynchronization.          |
| **Beta ($\beta$)**   | $5 - 20 \mu V$        | **Active Concentration / Anxiety:** Intense "busy" brain activity.              | **Deep Sleep:** Or when the motor cortex is at rest (SMR rhythm).                        |
| **Gamma ($\gamma$)** | $2 - 10 \mu V$        | **Complex Problem Solving:** Peak cognitive integration ("Aha!" moments).       | **General States:** Usually buried under noise; very hard to see without SNR processing. |
Note that during relaxation or low cognitive load, amplitudes are high as neurons are synchronized. In more cognitive load, neuron clusters perform multiple tasks and hence a neuron cluster may have multiple dipoles within it, so the overall amplitude of the cluster reduces.
# Attention Parameters

| **Type**        | **Description**                                                                     |
| --------------- | ----------------------------------------------------------------------------------- |
| **Focused**     | The ability to respond discretely to specific visual, auditory, or tactile stimuli. |
| **Selective**   | Maintaining focus on a single stimulus while ignoring distractions.                 |
| **Alternating** | Shifting focus between tasks that require different cognitive requirements.         |
| **Divided**     | Responding simultaneously to multiple tasks or demands (true multitasking).         |

| **Paradigm**       | **Key EEG Marker & Electrode**                                            | **Method (The Protocol)**                                                                                                                     |
| ------------------ | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Oddball**        | **P300** (Positive spike) at **$Pz, Cz$**                                 | You are presented with a sequence of repetitive stimuli (e.g., a "beep" every second). Occasionally, a different stimulus occurs (a "boop").  |
| **Stroop Task**    | **N450** (Negative deflection) & **Frontal $\theta$** at **$Fz, F3, F4$** | Display color names (e.g., "BLUE") where the ink color is different (e.g., Green). User must name the ink color while ignoring the text.      |
| **Task Switching** | **Switch-Related Negativity** & **$\alpha$ Suppression** at **$Fz, Pz$**  | Alternate between two different rules (e.g., odd/even vs. greater/less than 5). Measure the brain's "reconfiguration" time during the switch. |
| **Dual-Task**      | **Decreased ERP Amplitude** (Global/Distributed)                          | User performs a primary task while simultaneously responding to a secondary task (e.g., doing math while balancing on one leg).               |
