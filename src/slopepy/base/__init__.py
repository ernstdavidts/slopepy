from .analyzer import SlopeProtocolAnalyzer
"""
Base module for slopepy package.

This module provides core functionality for analyzing and visualizing slope protocols.
It exports the main analyzer class and plotting function for users to interact with
slope protocol data.

Classes:
    SlopeProtocolAnalyzer: Analyzer class for processing and analyzing slope protocol data.

Functions:
    plot_slope_protocol: Function to create visualizations of slope protocol results.
"""
from .plotter import plot_slope_protocol

__all__ = [
    "SlopeProtocolAnalyzer",
    "plot_slope_protocol",
] #Dit code definieert wat er wordt geëxporteerd wanneer iemand from slopepy.base import * doet.