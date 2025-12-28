#!/usr/bin/env python3
"""
Stack Overflow BS Detector
Because copy-pasting code should come with a warning label.
"""

import re
import sys
from datetime import datetime
from typing import List, Dict, Optional

class BSDetector:
    """Detects suspicious Stack Overflow patterns that scream 'bad idea'."""
    
    def __init__(self):
        # Classic red flags that make senior devs cry
        self.red_flags = [
            (r'\beval\b', "Using eval() - because security is overrated!"),
            (r'\bexec\b', "Found exec() - the 'hold my beer' of Python"),
            (r'\bfrom __future__ import\b', "Future import - this code is from the past!"),
            (r'\bimport os; os\.system\b', "Direct shell calls - what could go wrong?"),
            (r'\bwhile True:\s*break', "Infinite loop with break - peak efficiency!"),
            (r'\btry:\s*except:\s*pass', "Silent exception swallowing - problems solved!"),
            (r'\bglobal\b.*\bglobal\b', "Double global - because one wasn't confusing enough"),
            (r'\blambda.*lambda', "Nested lambdas - readability is for the weak!"),
            (r'200[0-9]', "Code from the 2000s - older than some interns!"),
        ]
    
    def analyze_code(self, code: str) -> List[Dict[str, str]]:
        """Find all the questionable life choices in this code."""
        issues = []
        
        for pattern, message in self.red_flags:
            if re.search(pattern, code, re.IGNORECASE):
                issues.append({
                    "severity": "BS",
                    "message": message,
                    "advice": "Consider if you really need this level of 'creativity'"
                })
        
        # Check for suspiciously short solutions
        lines = code.strip().split('\n')
        if len(lines) < 3 and 'def ' in code:
            issues.append({
                "severity": "SUS",
                "message": "One-liner function - either genius or madness",
                "advice": "If it looks too good to be true, it probably is"
            })
        
        return issues
    
    def generate_report(self, code: str) -> str:
        """Create a 'helpful' report about why you should reconsider."""
        issues = self.analyze_code(code)
        
        if not issues:
            return "No obvious BS detected. (But we're probably missing something)"
        
        report = ["\n🚨 STACK OVERFLOW BS DETECTOR REPORT 🚨",
                 "=" * 45,
                 f"Found {len(issues)} questionable pattern(s):\n"]
        
        for i, issue in enumerate(issues, 1):
            report.append(f"{i}. [{issue['severity']}] {issue['message']}")
            report.append(f"   💡 {issue['advice']}\n")
        
        report.append("\n⚠️  Remember: Just because it compiles doesn't mean it's a good idea!")
        report.append("📚 Consider: Reading the docs instead of Stack Overflow")
        
        return '\n'.join(report)


def main():
    """Main function - because every script needs one, apparently."""
    print("Stack Overflow BS Detector")
    print("Paste your suspicious code (Ctrl+D to finish):\n")
    
    try:
        code = sys.stdin.read()
    except KeyboardInterrupt:
        print("\n\nCancelled - probably for the best!")
        return
    
    if not code.strip():
        print("No code provided. Wise choice!")
        return
    
    detector = BSDetector()
    print(detector.generate_report(code))

if __name__ == "__main__":
    main()
