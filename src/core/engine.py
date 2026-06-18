"""
ThreatForge Engine Module
================================================================================
⚠️ LEGAL DISCLAIMER ⚠️
ThreatForge is for EDUCATIONAL and AUTHORIZED use only.
The authors assume NO LIABILITY for misuse.
================================================================================
"""
from rich.console import Console

console = Console()

class Engine:
    def __init__(self, verbose=False):
        self.verbose = verbose
        
    def run(self, mode='full', report_format='all'):
        console.print(f"Running pipeline in mode: {mode}")
        # Orchestration logic goes here
