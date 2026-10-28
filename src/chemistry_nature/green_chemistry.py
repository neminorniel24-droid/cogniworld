"""Green-chemistry metrics with explicit assumptions and scope."""
import math
from .formula import molar_mass, parse_formula

def atom_economy(*, reactants, desired_product, balanced_coefficients):
    """Theoretical atom economy when desired product is the only product.

    Coefficients are ordered as reactants followed by desired product. Does not
    include yield, solvent, process energy, or hazards.
    """
    if not reactants or not isinstance(desired_product,str) or not desired_product:
        raise ValueError("reactants and desired_product are required")
    formulas=list(reactants)+[desired_product]
    if len(balanced_coefficients)!=len(formulas): raise ValueError("one coefficient required per listed formula")
    if any(isinstance(c,bool) or not isinstance(c,int) or c<1 for c in balanced_coefficients):
        raise ValueError("coefficients must be positive integers")
    left={}
    for formula,coeff in zip(reactants,balanced_coefficients[:-1]):
        for e,n in parse_formula(formula).items(): left[e]=left.get(e,0)+n*coeff
    right={e:n*balanced_coefficients[-1] for e,n in parse_formula(desired_product).items()}
    if left!=right: raise ValueError("stoichiometry is not atom-balanced for listed reactants and desired product")
    denominator=sum(molar_mass(f)*c for f,c in zip(reactants,balanced_coefficients[:-1]))
    return 100*molar_mass(desired_product)*balanced_coefficients[-1]/denominator

def e_factor(*, waste_mass, product_mass):
    """E-factor = waste mass / product mass; caller must define waste boundary."""
    for name,value in (("waste_mass",waste_mass),("product_mass",product_mass)):
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<0:
            raise ValueError(f"{name} must be finite and non-negative")
    if product_mass<=0: raise ValueError("product_mass must be greater than zero")
    return float(waste_mass)/float(product_mass)
