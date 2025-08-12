#!/usr/bin/env python3
"""
Command Line Interface for Prompt Injection Core
"""

import argparse
import sys
import json
from typing import List
from .scanner.scanner import PromptScanner


def format_text_output(result, verbose: bool = False) -> str:
    """Format scan result as readable text"""
    lines = []
    
    # Header
    lines.append("=" * 60)
    lines.append("PROMPT INJECTION SECURITY SCAN")
    lines.append("=" * 60)
    
    # Basic info
    lines.append(f"Prompt: {result.prompt}")
    lines.append("")
    
    if result.vulnerabilities_found == 0:
        lines.append("✅ NO VULNERABILITIES DETECTED")
        lines.append("The prompt appears to be safe.")
    else:
        lines.append("🚨 VULNERABILITIES DETECTED:")
        
        # Show each detection
        for i, detection in enumerate(result.detections, 1):
            severity_emoji = {
                "CRITICAL": "🔴",
                "HIGH": "🟠", 
                "MEDIUM": "🟡",
                "LOW": "🟢"
            }.get(detection.severity, "⚪")
            
            lines.append(f"   {i}. {severity_emoji} {detection.vulnerability_type}")
            lines.append(f"      Severity: {detection.severity}")
            lines.append(f"      Confidence: {detection.confidence:.0%}")
            
            if verbose:
                lines.append(f"      Description: {detection.description}")
                lines.append(f"      Evidence: {detection.evidence}")
                lines.append("      Recommendations:")
                for rec in detection.recommendations:
                    lines.append(f"        • {rec}")
            lines.append("")
    
    # Summary
    lines.append(f"📊 RISK SCORE: {result.risk_score}/100")
    lines.append(f"📝 SUMMARY: {result.summary}")
    
    # Risk level indicator
    if result.risk_score >= 75:
        lines.append("⚠️  CRITICAL RISK - Immediate action required!")
    elif result.risk_score >= 50:
        lines.append("⚠️  HIGH RISK - Review and filter recommended")
    elif result.risk_score >= 25:
        lines.append("💡 MEDIUM RISK - Monitor for patterns")
    else:
        lines.append("✅ LOW/NO RISK - Prompt appears safe")
    
    lines.append("=" * 60)
    
    return "\n".join(lines)


def format_json_output(result) -> str:
    """Format scan result as JSON"""
    output = {
        "prompt": result.prompt,
        "risk_score": result.risk_score,
        "vulnerabilities_found": result.vulnerabilities_found,
        "summary": result.summary,
        "detections": [
            {
                "vulnerability_type": d.vulnerability_type,
                "severity": d.severity,
                "confidence": d.confidence,
                "description": d.description,
                "evidence": d.evidence,
                "recommendations": d.recommendations
            }
            for d in result.detections
        ]
    }
    return json.dumps(output, indent=2, ensure_ascii=False)


def scan_single_prompt(prompt: str, format_type: str, verbose: bool) -> None:
    """Scan a single prompt and display results"""
    scanner = PromptScanner()
    result = scanner.scan(prompt)
    
    if format_type == "json":
        print(format_json_output(result))
    else:
        print(format_text_output(result, verbose))


def scan_file(file_path: str, format_type: str, verbose: bool) -> None:
    """Scan prompts from a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            prompts = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        sys.exit(1)
    
    if not prompts:
        print("❌ Error: No prompts found in file")
        sys.exit(1)
    
    scanner = PromptScanner()
    
    if format_type == "json":
        # JSON format for multiple prompts
        results = []
        for prompt in prompts:
            result = scanner.scan(prompt)
            results.append({
                "prompt": result.prompt,
                "risk_score": result.risk_score,
                "vulnerabilities_found": result.vulnerabilities_found,
                "summary": result.summary,
                "detections": [
                    {
                        "vulnerability_type": d.vulnerability_type,
                        "severity": d.severity,
                        "confidence": d.confidence,
                        "description": d.description,
                        "evidence": d.evidence,
                        "recommendations": d.recommendations
                    }
                    for d in result.detections
                ]
            })
        
        output = {
            "total_prompts": len(prompts),
            "results": results
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
    
    else:
        # Text format for multiple prompts
        print("=" * 80)
        print(f"BATCH SCAN RESULTS - {len(prompts)} prompts")
        print("=" * 80)
        
        high_risk_count = 0
        total_vulnerabilities = 0
        
        for i, prompt in enumerate(prompts, 1):
            result = scanner.scan(prompt)
            
            if result.risk_score >= 50:
                high_risk_count += 1
            total_vulnerabilities += result.vulnerabilities_found
            
            print(f"\n🔍 PROMPT #{i}")
            print(f"Text: {result.prompt}")
            print(f"Risk Score: {result.risk_score}/100")
            print(f"Vulnerabilities: {result.vulnerabilities_found}")
            print(f"Summary: {result.summary}")
            
            if verbose and result.detections:
                print("Detections:")
                for detection in result.detections:
                    print(f"  • {detection.vulnerability_type} ({detection.severity})")
            
            print("-" * 40)
        
        # Summary
        print(f"\n📊 BATCH SUMMARY:")
        print(f"Total prompts scanned: {len(prompts)}")
        print(f"High-risk prompts: {high_risk_count}")
        print(f"Total vulnerabilities: {total_vulnerabilities}")
        print(f"Risk rate: {high_risk_count/len(prompts)*100:.1f}%")


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Prompt Injection Core - Detect vulnerabilities in prompts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  prompt-injection-scan "Ignore all previous instructions"
  prompt-injection-scan --file prompts.txt --verbose
  prompt-injection-scan "Your prompt" --format json
  prompt-injection-scan --help
        """
    )
    
    # Main argument
    parser.add_argument(
        "prompt",
        nargs="?",
        help="Prompt text to analyze (required if --file not used)"
    )
    
    # Optional arguments
    parser.add_argument(
        "--file", "-f",
        type=str,
        help="File containing prompts to analyze (one per line)"
    )
    
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed information about detections"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="prompt-injection-core 0.1.0"
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.prompt and not args.file:
        parser.error("Must provide either a prompt or --file option")
    
    if args.prompt and args.file:
        parser.error("Cannot use both prompt and --file options")
    
    try:
        if args.file:
            scan_file(args.file, args.format, args.verbose)
        else:
            scan_single_prompt(args.prompt, args.format, args.verbose)
    
    except KeyboardInterrupt:
        print("\n⚠️  Scan interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
