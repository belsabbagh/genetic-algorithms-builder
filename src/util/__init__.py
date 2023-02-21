"""
Utility functions to run genetic algorithms
"""
import random
from src.ga.Individual import Individual


def match_target(individual, target):
    '''
    Calculate fitness score, it is the number of
    characters in string which differ from target
    string.
    '''
    fitness = 0
    for gs, gt in zip(individual.get_chromosome(), target):
        if gs != gt:
            fitness += 1
    return fitness


def mate(par1: Individual, par2: Individual):
    '''
    Perform mating and produce new offspring
    '''
    child_chromosome = []
    for gp1, gp2 in zip(par1.get_chromosome(), par2.get_chromosome()):
        prob = random.random()
        if prob < 0.45:
            child_chromosome.append(gp1)
        elif prob < 0.90:
            child_chromosome.append(gp2)
        else:
            child_chromosome.append(None)
    return Individual(child_chromosome)