import itertools

import numpy as np

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def all_possible_evidence_variable_states(evidence_variables, *, variable_states):
    """
    For the given list of evidence variables, create a list of possible
    evidence variable states.
    """
    all_evidence_combinations = []
    for states in itertools.product(*[range(len(variable_states[x])) for x in evidence_variables]):
        # Create the evidence state
        evidence = {evidence_variables[var_idx]: variable_states[evidence_variables[var_idx]][var_state] 
                    for var_idx, var_state in enumerate(states)}
        all_evidence_combinations.append(evidence)
    return all_evidence_combinations

def get_cpt_from_bayesian_network(model: BayesianNetwork, *, variable, evidence_variables, variable_states):
    """
    Given a Bayesian network, compute any CPT.
    """
    # We will use variable elimination for inference
    inference = VariableElimination(model)

    # Get all possible envidence variable states
    all_evidence_states = all_possible_evidence_variable_states(evidence_variables, variable_states=variable_states)
    values = []
    for e in all_evidence_states:
        # Infer the state of variable given the evidence state
        values.append(inference.query(variables=[variable], evidence=e).values)
    probabilities = np.array(values).T

    # Create the CPT
    cpt = TabularCPD(
        variable=variable,
        variable_card=len(variable_states[variable]),
        values=probabilities,
        evidence=evidence_variables,
        evidence_card=[len(variable_states[e]) for e in evidence_variables],
        state_names=variable_states,
    )

    return cpt

def convert_cpts_from_source_model_to_target_model(source_model, target_model, *, variable_states):
    # Copy the target model
    target_model = target_model.copy()
    # Remove all CPTs in the target model (they are going to be replaced anyway)
    if len(target_model.cpds) > 0:
        target_model.remove_cpds([cpd.variable for cpd in target_model.cpds])

    # Compute each CPT from the source model
    for target_cpt in target_model.get_random_cpds().get_cpds():
        variable = target_cpt.variable
        evidence_variables = target_cpt.variables[1:]

        # Compute the target CPT from source model
        new_cpt = get_cpt_from_bayesian_network(source_model, 
                                                variable=variable, 
                                                evidence_variables=evidence_variables, 
                                                variable_states=variable_states)

        # Add the CPT to the target model
        target_model.add_cpds(new_cpt)

    return target_model

if __name__ == '__main__':
    pass
    # car_model_full_ = convert_cpts_from_source_model_to_target_model(car_model, car_model_full, variable_states=variable_states)
    # car_model_full_.save('heckermans-car-fully-connected-BayesNet.bif')
    # car_model_full_.load('heckermans-car-fully-connected-BayesNet.bif')