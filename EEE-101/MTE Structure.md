
---

## **Phase I: Foundations of Systems & Modeling**

*Before we control a system, we must define its nature and language.*

### **1. Introduction to Control Architectures**

* **Standard Block Model:** The universal language of control.
* **The Plant (System):** The physical entity being controlled.
* **Actuator:** The "muscle" that converts control signals into physical action.
* **Sensor:** The "eyes" that provide feedback.
* **Controller:** The "brain" that computes the error and necessary correction.


* **Topologies:**
* **Feed-forward:** Control based on anticipation/input (open-loop).
* **Feedback (Closed-loop):** Control based on the difference between desired and actual output (the error signal).



### **2. Classification of Systems**

* **Static vs. Dynamic:** Does the output depend only on the current input (Static/Memoryless) or also on past history (Dynamic/Memory)?
* **Causal vs. Non-causal:** A system is causal if the output depends only on present and past inputs (physically realizable).
* **Time-Varying vs. Time-Invariant (LTI):** Do the system parameters change over time?
* **Linear vs. Non-linear:** Does it follow Superposition and Homogeneity?
* **The Operator Form ():** Representing differential equations as linear operators.


* **Lumped vs. Distributed:** Are the properties concentrated at points (Lumped - ODEs) or spread across space (Distributed - PDEs)?
* **SISO vs. MIMO (MISO/SIMO):** Single-Input Single-Output vs. Multi-Input Multi-Output architectures.

### **3. Physical Modeling & Linearization**

* **Mechanical Systems:** Translating mass, springs, and dampers into differential equations.
* **Electrical Systems:** Modeling RLC circuits using Kirchhoff's laws.
* **Linearization:** Most real-world systems are non-linear. We will use Taylor Series expansion around an operating point to create linear approximations.

---

## **Phase II: The Transform Domain (Frequency Response)**

*Differential equations are hard; algebraic equations are easy. We use Laplace to bridge the gap.*

### **4. Transfer Function Representation**

* **Laplace & Inverse Laplace:** Converting time-domain signals  to -domain .
* **The Transfer Function ():** The ratio of the Laplace of the output to the Laplace of the input (with zero initial conditions).
* **Classification by Order:**
* **Proper:** Degree of Denominator  Degree of Numerator.
* **Strictly Proper:** Denominator degree  Numerator.
* **Bi-proper:** Degrees are equal.
* **Improper:** Numerator degree  Denominator (Hard to realize physically).



### **5. Diagrammatic Reductions**

* **Block Diagram Algebra:** Rules for Cascade, Parallel, and Feedback loop reduction.
* **Signal Flow Graphs (SFG):** A more "fluid" visualization.
* Definitions: Nodes, Branches, Forward Paths, and Loops.
* **Mason’s Gain Formula:** A singular algebraic method to find the total transfer function without step-by-step reduction.



---

## **Phase III: Time-Domain Analysis**

*How does the system behave when we actually "flip the switch"?*

### **6. Transient and Steady-State Response**

* **Forced vs. Natural Response:** The system's "personality" vs. its reaction to an external "shove."
* **First-Order Systems:** Characterized by the **Time Constant ()**, Rise Time, and Settling Time.
* **Second-Order Systems:** * **Parameters:** Natural Frequency () and Damping Ratio ().
* **Behaviors:** Underdamped, Overdamped, Critically Damped, and Undamped.
* **Performance Metrics:** Peak Time (), Percentage Overshoot (), Settling Time (), and Rise Time ().


* **Steady-State Error Analysis:** Evaluating the precision of a system after the transients have died down.

---

## **Phase IV: The Modern Approach (State-Space)**

#### **4.1. The State-Space Architecture**

We define the system using two fundamental equations. We will practice constructing these from $n^{th}$-order differential equations and RLC circuits.

- **The State Equation:** $\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t)$
    
- **The Output Equation:** $\mathbf{y}(t) = \mathbf{C}\mathbf{x}(t) + \mathbf{D}\mathbf{u}(t)$
    
    - **$\mathbf{A}$ (System Matrix, $n \times n$):** Defines the internal dynamics.
        
    - **$\mathbf{B}$ (Input Matrix, $n \times m$):** Defines how inputs affect the states.
        
    - **$\mathbf{C}$ (Output Matrix, $p \times n$):** Defines how states combine to form the output.
        
    - **$\mathbf{D}$ (Feedthrough Matrix, $p \times m$):** Direct coupling between input and output.
        

#### **4.2. Solving the Time-Domain State Equation**

How do we find $\mathbf{x}(t)$ if we know the initial state $\mathbf{x}(0)$ and the input $\mathbf{u}(t)$?

- **The General Solution:** $\mathbf{x}(t) = e^{\mathbf{A}t}\mathbf{x}(0) + \int_{0}^{t} e^{\mathbf{A}(t-\tau)}\mathbf{B}\mathbf{u}(\tau) d\tau$
    
- **Zero-Input Response (ZIR):** $e^{\mathbf{A}t}\mathbf{x}(0)$ — the system's "natural" decay from initial conditions.
    
- **Zero-State Response (ZSR):** The convolution integral — the system's reaction to the external "drive."
    

#### **4.3. The State Transition Matrix (STM): $\mathbf{\Phi}(t) = e^{\mathbf{A}t}$**

The STM is the "heart" of state-space. We will cover three methods to calculate it:

1. **The Power Series Method:** $e^{\mathbf{A}t} = \mathbf{I} + \mathbf{A}t + \frac{(\mathbf{A}t)^2}{2!} + \dots$
    
2. **The Laplace Transform Method:** $\mathbf{\Phi}(t) = \mathcal{L}^{-1}\{(\mathbf{sI} - \mathbf{A})^{-1}\}$
    
    - _Calculation:_ Finding the inverse of the characteristic matrix $(\mathbf{sI} - \mathbf{A})$.
        
3. **The Cayley-Hamilton Theorem:** Using the characteristic equation to simplify high-power matrices into a finite sum.
    

#### **4.4. Similarity Transformations & Canonical Forms**

Often, the original state variables are not physically intuitive. We can change our "viewpoint" using a transformation matrix $\mathbf{T}$, where $\mathbf{x} = \mathbf{T}\mathbf{z}$.

- **Transformed Matrices:** * $\mathbf{\bar{A}} = \mathbf{T}^{-1}\mathbf{AT}$
    
    - $\mathbf{\bar{B}} = \mathbf{T}^{-1}\mathbf{B}$
        
    - $\mathbf{\bar{C}} = \mathbf{CT}$
        
- **Diagonalization:** If $\mathbf{T}$ is the modal matrix (formed by eigenvectors of $\mathbf{A}$), then $\mathbf{\bar{A}}$ becomes a diagonal matrix of eigenvalues, decoupling the system equations.
    

#### **4.5. Converting to Transfer Functions**

We bridge the gap between Phase II and Phase IV using the **Resolvent Matrix**.

- **Formula:** $G(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$
    
- Note that the poles of the transfer function are exactly the **eigenvalues** of the matrix $\mathbf{A}$ (found by solving $\det(s\mathbf{I} - \mathbf{A}) = 0$).
    

#### **4.6. Controllability and Observability (System Properties)**

Before designing a controller, we must ask if it is even mathematically possible to control or see the states.

- **Controllability:** Can we move the system from any initial state to any final state in finite time?
    
    - **Controllability Matrix:** $\mathbf{Q}_c = [\mathbf{B} \mid \mathbf{AB} \mid \mathbf{A}^2\mathbf{B} \mid \dots \mid \mathbf{A}^{n-1}\mathbf{B}]$
        
    - _Requirement:_ $\text{rank}(\mathbf{Q}_c) = n$.
        
- **Observability:** Can we determine the internal states just by looking at the output $\mathbf{y}(t)$?
    
    - **Observability Matrix:** $\mathbf{Q}_o = [\mathbf{C}^T \mid \mathbf{A}^T\mathbf{C}^T \mid \dots \mid (\mathbf{A}^T)^{n-1}\mathbf{C}^T]^T$
        
    - _Requirement:_ $\text{rank}(\mathbf{Q}_o) = n$.

---

## **Phase V: Stability & Root Analysis**

*The most critical question: Will the system explode or settle?*

### **8. Stability Theory**

* **BIBO Stability:** Bounded-Input Bounded-Output.
* **Asymptotic Stability:** Does the natural response decay to zero?
* **Pole-Zero Plots:** Visualizing stability on the -plane.

### **9. Stability Tools**

* **Routh-Hurwitz Criterion:** A tabular method to determine stability without solving for roots.
* **Root Locus Technique:** A graphical method showing how the system's poles move as we vary the controller gain ().

---
