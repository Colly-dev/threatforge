#!/usr/bin/env python3
"""
ThreatForge — Cyber Threat Intelligence & IOC Correlation Platform

================================================================================
⚠️ LEGAL DISCLAIMER ⚠️

ThreatForge is a threat intelligence platform designed for EDUCATIONAL 
PURPOSES and AUTHORIZED SECURITY USE ONLY.

By using this software, you agree to:
- ONLY use threat intelligence data for legitimate security purposes
- Comply with all applicable laws and regulations
- Respect the terms of service of all data sources
- Accept full responsibility for your actions
- NOT use this tool for illegal or unauthorized activities

The authors assume NO LIABILITY for misuse, damage, or legal consequences
resulting from the use of this software.

USE RESPONSIBLY. STAY LEGAL. BE ETHICAL.
================================================================================
"""

import sys
import os
import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from core.engine import Engine

console = Console()

def print_banner():
    """Print the ThreatForge banner with legal disclaimer."""
    banner_text = """
  _____ _   _ ____  _____    _  _____ _____ ___  ____   ____ _____ 
 |_   _| | | |  _ \| ____|  / \|_   _|  ___/ _ \|  _ \ / ___| ____|
   | | | |_| | |_) |  _|   / _ \ | | | |_ | | | | |_) | |  _|  _|  
   | | |  _  |  _ <| |___ / ___ \| | |  _|| |_| |  _ <| |_| | |___ 
   |_| |_| |_|_| \_\_____/_/   \_\_| |_|   \___/|_| \_\\\\____|_____|
    """
    
    # Create the text objects with correct colors
    banner_obj = Text(banner_text, style="green")
    
    disclaimer_text = """
  ⚠️  LEGAL NOTICE - READ CAREFULLY  ⚠️                          
                                                                 
  ThreatForge is for EDUCATIONAL and AUTHORIZED use only.        
  Respect the terms of service of all data sources.              
                                                                 
  By using this tool you agree to:                               
    • Only use for legitimate security purposes                  
    • Comply with all laws and ToS                               
    • Accept full responsibility                                 
                                                                 
  The authors assume NO LIABILITY for misuse.                    
    """
    
    # Create the panel with white border
    panel = Panel(
        disclaimer_text,
        title=banner_obj,
        border_style="white",
        expand=False
    )
    
    console.print(panel)

@click.command()
@click.option('--mode', type=click.Choice(['collect', 'enrich', 'correlate', 'report', 'dashboard', 'monitor', 'full']), default='full', help='Operation mode')
@click.option('--format', type=click.Choice(['html', 'json', 'csv', 'all']), default='all', help='Report format')
@click.option('--ioc', type=str, help='Single IOC lookup')
@click.option('-v', '--verbose', is_flag=True, help='Enable verbose output')
def main(mode, format, ioc, verbose):
    """ThreatForge - Cyber Threat Intelligence Platform"""
    print_banner()
    
    try:
        engine = Engine(verbose=verbose)
        
        if ioc:
            console.print(f"[cyan]Performing single IOC lookup for: {ioc}[/cyan]")
            # Implement single IOC lookup logic
            pass
        else:
            console.print(f"[cyan]Starting ThreatForge in {mode} mode...[/cyan]")
            engine.run(mode=mode, report_format=format)
            
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)

if __name__ == '__main__':
    main()
