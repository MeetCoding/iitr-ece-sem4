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
