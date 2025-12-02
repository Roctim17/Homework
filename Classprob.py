import math

def hypothesis_testing_logistics_class(total_students=44, claimed_girls=1, sample_size=1, observed_girls=1):
    """
    Hypothesis test for number of girls in logistics class
    
    Args:
        total_students: Total number of students in class (44)
        claimed_girls: Claimed number of girls under null hypothesis (1)
        sample_size: Number of students sampled (1 in the example)
        observed_girls: Number of girls observed in sample (1 in the example)
    """
    
    print("=" * 50)
    print("HYPOTHESIS TESTING - LOGISTICS CLASS")
    print("=" * 50)
    
    # 1. Complete Event Group
    print("\n1. Complete Event Group:")
    print(f"- Total students: {total_students}")
    print(f"- Gender options: Boy or Girl")
    
    # 2. Hypotheses
    print("\n2. Hypotheses:")
    print(f"H0 (Null): There is only {claimed_girls} girl in the class")
    print(f"H1 (Alternative): There are more than {claimed_girls} girls in the class")
    
    # 3. Select Sample
    print(f"\n3. Select Sample:")
    print(f"- Sample size: {sample_size} student(s)")
    print(f"- Observed: {observed_girls} girl(s) in sample")
    
    # 4. Calculate Test Statistic (Probability)
    print(f"\n4. Calculate Probability:")
    
    # If H0 is true (only 1 girl), probability of drawing a girl in one sample
    p_value = claimed_girls / total_students
    print(f"Under H0, probability of selecting a girl = {claimed_girls}/{total_students}")
    print(f"P-value = {p_value:.4f}")
    
    # 5. Decision Rule
    print(f"\n5. Decision Rule:")
    print(f"   Significance level (α) = 0.05")
    print(f"   If P < 0.05, reject H0")
    print(f"   If P ≥ 0.05, fail to reject H0")
    
    # 6. Conclusion
    print(f"\n6. Conclusion:")
    if p_value < 0.05:
        print(f"Since P = {p_value:.4f} < 0.05")
        print(f"✓ REJECT the null hypothesis")
        print(f"✓ ACCEPT the alternative hypothesis")
        print(f"There is statistically significant evidence that")
        print(f"there are more than {claimed_girls} girl(s) in the class.")
    else:
        print(f"Since P = {p_value:.4f} ≥ 0.05")
        print(f"✗ FAIL TO REJECT the null hypothesis")
        print(f"Not enough evidence to say there are more than {claimed_girls} girl(s).")
    
    return p_value

def calculate_rejection_region(total_students=44, alpha=0.05):
    """Calculate the rejection region for different sample sizes"""
    print("\n" + "=" * 50)
    print("REJECTION REGION ANALYSIS")
    print("=" * 50)
    
    print("\nIf H0 is true (only 1 girl out of 44):")
    p_girl = 1/44
    
    for sample_size in [1, 5, 10, 20]:
        print(f"\nSample size: {sample_size}")
        print(f"  Probability of getting all girls in sample: {(p_girl)**sample_size:.6f}")
        
        # Critical value for binomial test
        import scipy.stats as stats
        if sample_size > 1:
            # For larger samples, we'd use binomial test
            critical_value = stats.binom.ppf(1-alpha, sample_size, p_girl)
            print(f"  Would need > {critical_value:.1f} girls to reject H0 at α={alpha}")

# Run the example from the image
if __name__ == "__main__":
    # Example from image: 44 students, claim of 1 girl, sample 1 student who is a girl
    p = hypothesis_testing_logistics_class(
        total_students=44,
        claimed_girls=1,
        sample_size=1,
        observed_girls=1
    )
    
    # Calculate rejection regions
    calculate_rejection_region()
    
    # Interactive version
    print("\n" + "=" * 50)
    print("INTERACTIVE TESTING")
    print("=" * 50)
    
    # Try different scenarios
    scenarios = [
        (44, 1, 1, 1),  # Original example
        (44, 1, 5, 3),  # Sample 5, get 3 girls
        (44, 5, 10, 6), # Claim: 5 girls, sample 10, get 6
    ]
    
    for total, claimed, sample, observed in scenarios:
        print(f"\nScenario: {total} students, claim: {claimed} girl(s)")
        print(f"Sample: {sample} students, observed: {observed} girl(s)")
        hypothesis_testing_logistics_class(total, claimed, sample, observed)