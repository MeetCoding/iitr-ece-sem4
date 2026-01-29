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

# Attention Parameters

