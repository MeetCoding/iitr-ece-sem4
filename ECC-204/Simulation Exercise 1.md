***Meet Shah, 24116051***

![[Pasted image 20260129150412.png]]

# Problem 1

We start by placing a `nmos4` component on our LTSpice Schematic sheet, and connect a voltage source `V_DS` to its drain terminal and `V_GS` to its gate terminal. We short the source terminal and the body:

![[Pasted image 20260129153657.png]]
We also set the width and length of the NMOS to the given values:

![[Pasted image 20260129153619.png]]

We then add the simulation configuration to use a linear curve from $0V$ to $1.8V$ for $V_{GS}$ and a list of $[0V, 0.9V, 1.8V]$ for $V_{DS}$, and run the simulation:

![[Pasted image 20260129153542.png]]

However, the parameters of the `nmos4` are not adjusted according to the TSMC 180nm technology `nmos` mentioned in the question, so we add the model file for the TSMC `nmos` and plot the new graph:

`.model TSMC_NMOS NMOS(Level=1 Vto=0.45 KP=170u Lambda=0.05)`

![[Pasted image 20260129154208.png]]

We can see that the cutoff voltage is around $0.5V$.

Changing the DC Sweep values for $V_{GS}$ (now $[0V,0.8V,1.4V]$) and $V_{DS}$ (now linear from $0V-1.8V$), we get the following characteristic:

![[Pasted image 20260129164158.png]]

We can here clearly see the cutoff, linear/triode and saturation region.
- For $V_{GS}=0V$, the transistor is in cutoff region.
- For $V_{GS}=0.8V$, the graph is saturated at $V_{DS}=0.3V$
- For $V_{GS}=1.4V$, the graph is saturated at $V_{DS}=1V$
Note that the values above are approximations and not exact.

Repeating the experiment for PMOS:

![[Pasted image 20260129170042.png]]

We find similar cutoff voltage at about $0.5V$.

![[Pasted image 20260129170140.png]]

We also see similar cutoff values as that of NMOS.

We know the relation: $I_D=\dfrac{1}{2}\mu_nC_{ox}\dfrac{W}{L}(V_{GS}-V_{Th})^2(1+\lambda_n V_{DS})$ for a NMOS transistor.
We know that $V_{GS}>V_{Th}$, and $V_{Th}=0.45V$, so $V_{GS}>0.45V$
We also know that for saturation, $V_{DS}>V_{GS}-V{Th}\implies V_{GS}<V_{DS}+0.45V$

1. When $V_{DS}=0V\implies V_{GS}<0.45V$ (Not possible)
2. When $V_{DS}=0.9V\implies V_{GS}<1.35V$
3. When $V_{DS}=1.8V\implies V_{GS}<2.25V$

Hence, we have two variables, $\mu_nC_{ox}$ and $\lambda$ and two equations from (2) and (3).

At same $V_{GS}$, $\dfrac{I_{D1}}{I_{D2}}=\dfrac{1+\lambda V_{DS1}}{1+\lambda V_{DS2}}$
For $I_{D1}=452.26\mu A$ and $V_{DS1}=1.2V$
For $I_{D2}=456.55\mu A$ and $V_{DS2}=1.4V$
Putting the values, we get, $\lambda = 0.0503$

$\mu_nC_{ox}=\dfrac{2L}{W}\dfrac{I_D}{(V_{GS}-0.45)^2(1+0.0503V_{DS})}$
We know, $I_D=452.26, V_{DS}=1.2V, V_{GS}=1.4V, L=0.18um, W=1um$
Hence, we get, $\mu_nC_{ox}=1.7e-4=170\mu A/V^2$

Marking values for PMOS, we get:

| **I_D**  | $159.51\mu A$ | $161.05\mu A$ | $21.59\mu A$ |
| -------- | ------------- | ------------- | ------------ |
| **V_DS** | $1.2V$        | $1.4V$        | $1.2V$       |
| **V_GS** | $1.4V$        | $1.4V$        | $0.8V$       |

By doing the same calculation as done previously for NMOS, we will get:
- $\lambda_p = 0.0512$
- $\mu_pC_{ox}=70 \mu A/V^2$

The calculated values of $\lambda$ and $K_p=\mu C_{ox}$ are nearly same to the values defined in the model file (slight variation due to calculation errors).

```
.model TSMC_NMOS NMOS(Level=1 Vto=0.45 KP=170u Lambda=0.05)
.model TSMC_PMOS PMOS(Level=1 Vto=-0.45 KP=60u Lambda=0.05)
```

Meaning of Level 1: 