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

Changing the DC Sweep values for $V_{GS}$ (now $[0V,0.8V,1.4V]$) and $V_{DS}$ (now )