import React from 'react';

const RiskAnalysis = () => {
    const riskMetrics = {
        likelihood: 0.7,
        impact: 0.6,
        riskLevel: 'Moderate',
    };

    return (
        <div className="risk-analysis">
            <h2>Risk Analysis</h2>
            <p>Likelihood: {riskMetrics.likelihood * 100}%</p>
            <p>Impact: {riskMetrics.impact * 100}%</p>
            <p>Risk Level: {riskMetrics.riskLevel}</p>
        </div>
    );
};

export default RiskAnalysis;