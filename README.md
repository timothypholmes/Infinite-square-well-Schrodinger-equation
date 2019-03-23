# Infinite-square-well-Schrodinger-equation
Analytical solution to the Time-Dependent Schrodinger equation for a particle in an infinite square well.

### Animation speed up 3000%
![time_dependent_3000](https://github.com/timothypholmes/Infinite-square-well-Schrodinger-equation/blob/master/time_dependent_3000.gif)

## The theory

Solving energy eigenvalues and eigenstates are used to understand the future of a physical system in quantum mechanics. The Schrödinger equation is the tool that allows for time evolution where the equation is,

<p align="center"><img src="/tex/d84c8f8ee4e3aa8882761665bdb2ee09.svg?invert_in_darkmode&sanitize=true" align=middle width=398.66734710000003pt height=33.81208709999999pt/></p>

When the Schrödinger equation is time-dependent, the solution becomes

<p align="center"><img src="/tex/3436aa1412a9f1263c8cf53cb314561e.svg?invert_in_darkmode&sanitize=true" align=middle width=437.2538907pt height=19.526994300000002pt/></p>

Therefore, when <img src="/tex/477a717e18587a5e8605780ca167c322.svg?invert_in_darkmode&sanitize=true" align=middle width=36.07293689999999pt height=21.18721440000001pt/> and <img src="/tex/08fbd8ec77aff96736a2f25a1ea90009.svg?invert_in_darkmode&sanitize=true" align=middle width=32.30223149999999pt height=24.65753399999998pt/> becomes

\being{equation}
\ket{\psi(0)} = \Sigma_n C_{n} \ket{E_n}
\end{equation}

since <img src="/tex/7e371e5bfb5c2c6f4f36d5ea24f1f488.svg?invert_in_darkmode&sanitize=true" align=middle width=67.58008619999998pt height=39.45205440000001pt/>\psi(x,0)<img src="/tex/b6bfc1ac7fa018c628b2dac4f9d06efd.svg?invert_in_darkmode&sanitize=true" align=middle width=1623.9040933499998pt height=167.4436797pt/>\psi(x,0) is normalized as the first step, the energy eigenstate wave functions are then found. Again, the energy eigenstate wave function need to be normailized and the following equation is derived,

<p align="center"><img src="/tex/754f1d0c7311297aa8de8ebe13cb160a.svg?invert_in_darkmode&sanitize=true" align=middle width=191.49886304999998pt height=39.452455349999994pt/></p>

Discrete quantized wave vectors are required to solve the Time-Dependent equation, <img src="/tex/65388eac83fde2cd79458efe154770d5.svg?invert_in_darkmode&sanitize=true" align=middle width=46.719990899999985pt height=24.65753399999998pt/>. The energy quantization for the system becomes,

<p align="center"><img src="/tex/eac2ec04d6bb17cbb83a4a670dd86600.svg?invert_in_darkmode&sanitize=true" align=middle width=102.3433653pt height=35.77743345pt/></p>

Finally, the last item the time dependent Schrödinger equation depends on is <img src="/tex/269df1b24837e284ec791de3ae768620.svg?invert_in_darkmode&sanitize=true" align=middle width=19.87487204999999pt height=22.465723500000017pt/>. <img src="/tex/86d578c943ecac4e464bf04be86c4b7b.svg?invert_in_darkmode&sanitize=true" align=middle width=42.882704699999984pt height=22.465723500000017pt/> is the expansion coefficient that chages the probability amplitude. The indefinite integral of the complex conjugate of eigenstate wave function and the initial wave function with respect to the spatial dimension x,

<p align="center"><img src="/tex/6bcd611f13835943a5dc1545b9eaec6c.svg?invert_in_darkmode&sanitize=true" align=middle width=195.01161405pt height=39.61228755pt/></p>

From equation (2): we bring together, <img src="/tex/fb02ec93ec494888822d01225b9c0ccc.svg?invert_in_darkmode&sanitize=true" align=middle width=41.881791599999985pt height=24.65753399999998pt/>, <img src="/tex/c01241b79d48a987aa4a4fbc5b05808a.svg?invert_in_darkmode&sanitize=true" align=middle width=20.26074269999999pt height=22.465723500000017pt/>, and <img src="/tex/fe6a8e7ea5ac601d9dd986902ca41d13.svg?invert_in_darkmode&sanitize=true" align=middle width=15.239827349999992pt height=14.15524440000002pt/>. The result is

<p align="center"><img src="/tex/5b91acd54e1af2411b569c559a41190e.svg?invert_in_darkmode&sanitize=true" align=middle width=217.72847744999996pt height=46.867754999999995pt/></p>

Now, as t increase the future of wave equation is determined as shown below in the animation. 

### Animation real time
![time_evolution](https://github.com/timothypholmes/Infinite-square-well-Schrodinger-equation/blob/master/time_evolution.gif)
