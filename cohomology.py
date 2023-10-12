''' These lists of data and instruction are designed to compute Betti numbers of certain torsion-free nilpotent groups using SAGE.
The groups are central products; their Dehn functions are determined in the paper ``On the Dehn functions of central products of nilpotent groups''.

To every such group, the Mal'cev theorem associates a rational Lie algebra, and these are also the Betti numbers of the Chevalley-Eilenberg complex for the Lie algebra cohomology of the Lie algebra.

Precisely, the input is a Lie algebra, encoded as a list of generators and brackets. 
Since the list of brackets may be long we define it first. 
For groups with low nilpotency class or short enough presentation, the list of brackets may be determined directly from the group presentation if it involves only relations of the form [x_i, x_j] = x_k or [x_i, x_j] = 1, where x_i, x_j and x_k are generators. 
In general one should beware that it is not the case, and one should use the Baker--Campbell--Hausdorff formula to translate lists of brackets into presentations.

As an example, consider the following declarations:

brackets = {
	('X_1','X_2') : {'X_3': 1},
	}
L.<X_1,X_2,X_3,X_4,Y_1,Y_2,Y_3> = LieAlgebra(QQ, brackets, nilpotent=True);L;

Here L will be the Heisenberg Lie algebra, with generators $X_1, X_2, X_3$ and nonzero bracket $[X_1,X_2] = X_3$, the other brackets being zero.

The list of Betti numbers is then the output of the instruction

Betti=[L.chevalley_eilenberg_complex().betti(i) for i in range(L.dimension()+1)];Betti;

The notations for the names of the groups are the ones from the paper cited above.
'''

# $L_{4,3} \times_Z L_{4,3}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'X_4': 1},
    }
    
L.<X_1,X_2,X_3,X_4,Y_1,Y_2,Y_3> = LieAlgebra(QQ, brackets, nilpotent=True);L;


# $L_{5,5} \times_Z L_{3,2}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_2','X_5') : {'X_4': 1},
    ('Y_1','Y_2') : {'X_4': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,Y_1,Y_2> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $L_{5,5} \times_Z L_{4,3}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_2','X_5') : {'X_4': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'X_4': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,Y_1,Y_2,Y_3> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $L_{5,5} \times_Z L_{5,5}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_2','X_5') : {'X_4': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'X_4': 1},
    ('Y_2','Y_5') : {'X_4': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,Y_1,Y_2,Y_3,Y_5> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $L_{4,3} \times_Z L_{4,3} \times \mathbf Z^2$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'X_4': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,Y_1,Y_2,Y_3,Y_5> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $L_{5,5} \times_Z L_{5,4}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_2','X_5') : {'X_4': 1},
    ('Y_1','Y_2') : {'X_4': 1},
    ('W_1','W_2') : {'X_4': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,Y_1,Y_2,W_1,W_2> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $L_{5,6} \times_Z L_{3,2}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('Y_1','Y_2') : {'X_5': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,Y_1,Y_2> = LieAlgebra(QQ, brackets, nilpotent=True);L;


# $L_{5,7} \times_Z L_{3,2}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('Y_1','Y_2') : {'X_5': 1},
    ('X_2','X_3') : {'X_5': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,Y_1,Y_2> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $L_{5,6} \times_Z L_{4,3}$, also called $G_{5,4}^{\lrcorner}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'X_5': 1},
    ('X_2','X_3') : {'X_5': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,Y_1,Y_2> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $L_{5,6} \times_Z L_{5,5}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'X_5': 1},
    ('Y_2','Y_5') : {'X_5': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,Y_1,Y_2,Y_3,Y_5> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $L_{5,7} \times_Z L_{5,5}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'X_5': 1},
    ('Y_2','Y_5') : {'X_5': 1},
    ('X_2','X_3') : {'X_5': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,Y_1,Y_2,Y_3,Y_5> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $G_{6,3}^{\lrcorner}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('X_1','X_5') : {'X_6': 1},
    ('Y_1','Y_2') : {'X_6': 1},
    ('X_2','X_3') : {'X_6': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,X_6,Y_1,Y_2> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $G_{6,3}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('X_1','X_5') : {'X_6': 1},
    ('Y_1','Y_2') : {'X_6': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,X_6,Y_1,Y_2> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $G_{6,4}^{\lrcorner}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('X_1','X_5') : {'X_6': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'X_6': 1},
    ('X_2','X_3') : {'X_6': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,X_6,Y_1,Y_2,Y_3> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $G_{6,4}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('X_1','X_5') : {'X_6': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'X_6': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,X_6,Y_1,Y_2,Y_3> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# The Carnot-graded group $\operatorname{gr}(G_{6,4}) = L_6 \times L_3$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('X_1','X_5') : {'X_6': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,X_6,Y_1,Y_2,Y_3> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $G_{6,5}^{\lrcorner}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('X_1','X_5') : {'X_6': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'Y_4': 1},
    ('Y_1','Y_4') : {'X_6': 1},
    ('X_2','X_3') : {'X_6': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,X_6,Y_1,Y_2,Y_3,Y_4> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $G_{6,5}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('X_1','X_5') : {'X_6': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'Y_4': 1},
    ('Y_1','Y_4') : {'X_6': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,X_6,Y_1,Y_2,Y_3,Y_4> = LieAlgebra(QQ, brackets, nilpotent=True);L;


# $G_{6,6}^\lrcorner$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('X_1','X_5') : {'X_6': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'Y_4': 1},
    ('Y_1','Y_4') : {'Y_5': 1},
    ('Y_1','Y_5') : {'X_6': 1},
    ('X_2','X_3') : {'X_6': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,X_6,Y_1,Y_2,Y_3,Y_4,Y_5> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $G_{7,6}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('X_1','X_5') : {'X_6': 1},
    ('X_1','X_6') : {'X_7': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'Y_4': 1},
    ('Y_1','Y_4') : {'Y_5': 1},
    ('Y_1','Y_5') : {'X_7': 1},
    ('X_2','X_3') : {'X_7': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,X_6,X_7,Y_1,Y_2,Y_3,Y_4,Y_5> = LieAlgebra(QQ, brackets, nilpotent=True);L;


# G_{7,5}^{\lrcorner}

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('X_1','X_5') : {'X_6': 1},
    ('X_1','X_6') : {'X_7': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'Y_4': 1},
    ('Y_1','Y_4') : {'X_7': 1},
    ('X_2','X_3') : {'X_7': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,X_6,X_7,Y_1,Y_2,Y_3,Y_4> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $G_{7,5}

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('X_1','X_5') : {'X_6': 1},
    ('X_1','X_6') : {'X_7': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'Y_4': 1},
    ('Y_1','Y_4') : {'X_7': 1},
    };
    
L.<X_1,X_2,X_3,X_4,X_5,X_6,X_7,Y_1,Y_2,Y_3,Y_4> = LieAlgebra(QQ, brackets, nilpotent=True);L;
Betti=[L.chevalley_eilenberg_complex().betti(i) for i in range(L.dimension()+1)];Betti;


# G_{7,4}^{\lrcorner}

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('X_1','X_5') : {'X_6': 1},
    ('X_1','X_6') : {'X_7': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'X_7': 1},
    ('X_2','X_3') : {'X_7': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,X_6,X_7,Y_1,Y_2,Y_3> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $G_{7,4}

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('X_1','X_5') : {'X_6': 1},
    ('X_1','X_6') : {'X_7': 1},
    ('Y_1','Y_2') : {'Y_3': 1},
    ('Y_1','Y_3') : {'X_7': 1},
    };
    
L.<X_1,X_2,X_3,X_4,X_5,X_6,X_7,Y_1,Y_2,Y_3> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# G_{7,3}^{\lrcorner}

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('X_1','X_4') : {'X_5': 1},
    ('X_1','X_5') : {'X_6': 1},
    ('X_1','X_6') : {'X_7': 1},
    ('Y_1','Y_2') : {'X_7': 1},
    ('X_2','X_3') : {'X_7': 1},
    }
    
L.<X_1,X_2,X_3,X_4,X_5,X_6,X_7,Y_1,Y_2> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $L_{4,3} \times_Z L_{5,4}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('Y_1','Y_2') : {'X_4': 1},
    ('Y_5','Y_6') : {'X_4': 1},
    }
    
L.<X_1,X_2,X_3,X_4,Y_1,Y_2,Y_3,Y_5,Y_6> = LieAlgebra(QQ, brackets, nilpotent=True);L;

# $L_{4,3} \times_Z L_{5,4} \times_Z L_{3,2}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('Y_1','Y_2') : {'X_4': 1},
    ('Y_5','Y_6') : {'X_4': 1},
    ('Y_7','Y_8') : {'X_4': 1},
    }
L.<X_1,X_2,X_3,X_4,Y_1,Y_2,Y_3,Y_5,Y_6,Y_7,Y_8> = LieAlgebra(QQ, brackets, nilpotent=True);L;


# $L_{4,3} \times_Z L_{5,4} \times_Z L_{5,4}$

brackets = {
    ('X_1','X_2') : {'X_3': 1},
    ('X_1','X_3') : {'X_4': 1},
    ('Y_1','Y_2') : {'X_4': 1},
    ('Y_4','Y_5') : {'X_4': 1},
    ('Y_6','Y_7') : {'X_4': 1},
    ('Y_8','Y_9') : {'X_4': 1},
    }
L.<X_1,X_2,X_3,X_4,Y_1,Y_2,Y_3,Y_5,Y_6,Y_7,Y_9> = LieAlgebra(QQ, brackets, nilpotent=True);L;




