#!/usr/bin/env python3
"""
Generate advanced mathematics training data inspired by Google DeepMind Mathematics Dataset
Creates comprehensive math problems across multiple categories
"""

import random
import math

def generate_algebra_problems(count=100):
    """Generate algebra problems"""
    problems = []
    
    for _ in range(count):
        # Linear equations: ax + b = c
        a = random.randint(2, 10)
        b = random.randint(1, 20)
        x = random.randint(1, 10)
        c = a * x + b
        
        problems.append(f"Solve {a}x + {b} = {c}. Answer: x = {x}")
        problems.append(f"What is x in {a}x + {b} = {c}? {x}")
        problems.append(f"If {a}x + {b} = {c}, then x = {x}")
        
        # Two variable equations
        a1, b1, c1 = random.randint(2, 5), random.randint(2, 5), random.randint(10, 30)
        a2, b2, c2 = random.randint(2, 5), random.randint(2, 5), random.randint(10, 30)
        
        # Ensure solvable
        det = a1 * b2 - a2 * b1
        if det != 0:
            x = random.randint(1, 5)
            y = random.randint(1, 5)
            c1 = a1 * x + b1 * y
            c2 = a2 * x + b2 * y
            
            problems.append(f"Solve {a1}x + {b1}y = {c1} and {a2}x + {b2}y = {c2} for x. Answer: x = {x}")
            problems.append(f"Find x: {a1}x + {b1}y = {c1}, {a2}x + {b2}y = {c2}. x = {x}")
    
    return problems

def generate_arithmetic_problems(count=100):
    """Generate arithmetic problems with multiple operations"""
    problems = []
    
    for _ in range(count):
        # Mixed operations
        numbers = [random.randint(1, 20) for _ in range(3)]
        ops = ['+', '-', '×']
        
        # Generate expressions like a + b × c
        a, b, c = numbers
        op1, op2 = random.sample(ops, 2)
        
        if op2 == '×':
            result = a + b * c
            problems.append(f"What is {a} + {b} × {c}? {result}")
            problems.append(f"Calculate {a} + {b} × {c}. Answer: {result}")
        elif op1 == '×' and op2 == '+':
            result = a * b + c
            problems.append(f"What is {a} × {b} + {c}? {result}")
            problems.append(f"Compute {a} × {b} + {c}. {result}")
        
        # Division with remainders
        dividend = random.randint(20, 100)
        divisor = random.randint(2, 10)
        quotient = dividend // divisor
        remainder = dividend % divisor
        
        problems.append(f"What is {dividend} ÷ {divisor}? {quotient} R {remainder}")
        problems.append(f"Divide {dividend} by {divisor}. Answer: {quotient} remainder {remainder}")
        
        # Fraction operations
        num1, den1 = random.randint(1, 9), random.randint(2, 10)
        num2, den2 = random.randint(1, 9), random.randint(2, 10)
        
        # Addition: a/b + c/d
        common_den = den1 * den2
        common_num = num1 * den2 + num2 * den1
        
        problems.append(f"What is {num1}/{den1} + {num2}/{den2}? {common_num}/{common_den}")
        problems.append(f"Add {num1}/{den1} and {num2}/{den2}. Answer: {common_num}/{common_den}")
    
    return problems

def generate_calculus_problems(count=50):
    """Generate basic calculus problems"""
    problems = []
    
    for _ in range(count):
        # Basic derivatives: ax^n
        a = random.randint(1, 5)
        n = random.randint(1, 4)
        derivative_coeff = a * n
        derivative_power = n - 1
        
        if derivative_power == 0:
            derivative = f"{derivative_coeff}"
        elif derivative_power == 1:
            derivative = f"{derivative_coeff}x"
        else:
            derivative = f"{derivative_coeff}x^{derivative_power}"
        
        problems.append(f"What is the derivative of {a}x^{n}? {derivative}")
        problems.append(f"d/dx({a}x^{n}) = {derivative}")
        problems.append(f"Differentiate {a}x^{n}. Answer: {derivative}")
        
        # Simple polynomials
        terms = []
        derivative_terms = []
        
        for _ in range(random.randint(2, 3)):
            coeff = random.randint(1, 5)
            power = random.randint(0, 3)
            
            if power == 0:
                terms.append(f"{coeff}")
            elif power == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{power}")
            
            if power > 0:
                deriv_coeff = coeff * power
                deriv_power = power - 1
                
                if deriv_power == 0:
                    derivative_terms.append(f"{deriv_coeff}")
                elif deriv_power == 1:
                    derivative_terms.append(f"{deriv_coeff}x")
                else:
                    derivative_terms.append(f"{deriv_coeff}x^{deriv_power}")
        
        function = " + ".join(terms)
        derivative = " + ".join(derivative_terms)
        
        problems.append(f"What is the derivative of {function}? {derivative}")
        problems.append(f"d/dx({function}) = {derivative}")
    
    return problems

def generate_geometry_problems(count=50):
    """Generate geometry problems"""
    problems = []
    
    for _ in range(count):
        # Area and perimeter
        length = random.randint(5, 20)
        width = random.randint(5, 20)
        
        area = length * width
        perimeter = 2 * (length + width)
        
        problems.append(f"What is the area of a rectangle with length {length} and width {width}? {area}")
        problems.append(f"Find the perimeter of a rectangle {length} by {width}. Answer: {perimeter}")
        
        # Circle problems
        radius = random.randint(3, 15)
        circumference = round(2 * math.pi * radius, 2)
        area_circle = round(math.pi * radius * radius, 2)
        
        problems.append(f"What is the circumference of a circle with radius {radius}? {circumference}")
        problems.append(f"Find the area of a circle radius {radius}. Answer: {area_circle}")
        
        # Triangle area
        base = random.randint(5, 20)
        height = random.randint(5, 20)
        triangle_area = (base * height) // 2
        
        problems.append(f"What is the area of a triangle with base {base} and height {height}? {triangle_area}")
        problems.append(f"Triangle area: base {base}, height {height}. Answer: {triangle_area}")
    
    return problems

def generate_number_theory_problems(count=50):
    """Generate number theory problems"""
    problems = []
    
    for _ in range(count):
        # Prime checking
        num = random.choice([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
        composite = random.choice([4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30])
        
        problems.append(f"Is {num} prime? True")
        problems.append(f"Is {composite} prime? False")
        
        # Factor problems
        n = random.randint(10, 50)
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        
        problems.append(f"What are the factors of {n}? {factors}")
        problems.append(f"List all factors of {n}. Answer: {factors}")
        
        # GCD problems
        a, b = random.randint(10, 50), random.randint(10, 50)
        
        # Calculate GCD
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        g = gcd(a, b)
        problems.append(f"What is the GCD of {a} and {b}? {g}")
        problems.append(f"Find GCD({a}, {b}). Answer: {g}")
    
    return problems

def generate_word_problems(count=50):
    """Generate mathematical word problems"""
    problems = []
    
    for _ in range(count):
        # Rate problems
        speed = random.randint(30, 80)
        time = random.randint(1, 6)
        distance = speed * time
        
        problems.append(f"If a car travels at {speed} mph for {time} hours, how far does it travel? {distance} miles")
        problems.append(f"Car speed: {speed} mph, time: {time} hours. Distance: {distance} miles")
        
        # Ratio problems
        ratio1, ratio2 = random.randint(2, 5), random.randint(2, 5)
        total = random.randint(20, 50)
        
        part1 = total * ratio1 // (ratio1 + ratio2)
        part2 = total - part1
        
        problems.append(f"If something is divided in ratio {ratio1}:{ratio2} and total is {total}, what is the first part? {part1}")
        problems.append(f"Ratio {ratio1}:{ratio2}, total {total}. First part: {part1}")
        
        # Percentage problems
        percent = random.randint(10, 50)
        whole = random.randint(100, 500)
        part = whole * percent // 100
        
        problems.append(f"What is {percent}% of {whole}? {part}")
        problems.append(f"Calculate {percent}% of {whole}. Answer: {part}")
    
    return problems

def main():
    """Generate all mathematics problems"""
    print("Generating advanced mathematics training data...")
    
    all_problems = []
    
    # Generate problems from each category
    all_problems.extend(generate_algebra_problems(100))
    all_problems.extend(generate_arithmetic_problems(100))
    all_problems.extend(generate_calculus_problems(50))
    all_problems.extend(generate_geometry_problems(50))
    all_problems.extend(generate_number_theory_problems(50))
    all_problems.extend(generate_word_problems(50))
    
    # Add some basic problems for robustness
    basic_problems = [
        "What is 2 + 2? 4",
        "What is 3 + 3? 6",
        "What is 4 + 4? 8",
        "What is 5 + 5? 10",
        "What is 10 - 2? 8",
        "What is 10 - 3? 7",
        "What is 2 × 3? 6",
        "What is 3 × 4? 12",
        "What is 4 × 5? 20",
        "What is 15 ÷ 3? 5",
        "What is 20 ÷ 4? 5",
        "What is 25 ÷ 5? 5"
    ]
    
    all_problems.extend(basic_problems)
    
    # Shuffle the problems
    random.shuffle(all_problems)
    
    # Save to file
    with open('advanced_mathematics_dataset.txt', 'w', encoding='utf-8') as f:
        for problem in all_problems:
            f.write(problem + '\n')
    
    print(f"Generated {len(all_problems)} advanced mathematics training examples")
    print("Categories covered:")
    print("- Algebra (linear equations, systems)")
    print("- Arithmetic (mixed operations, fractions)")
    print("- Calculus (basic derivatives)")
    print("- Geometry (area, perimeter, circles)")
    print("- Number Theory (primes, factors, GCD)")
    print("- Word Problems (rates, ratios, percentages)")
    print(f"Saved to advanced_mathematics_dataset.txt")
    
    return len(all_problems)

if __name__ == "__main__":
    main()
