window.onload = function() {
    fetch('EthicsReport.json')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(ethicsReport => {
            // Container
            let container = document.createElement('div');
            container.classList.add('container');
            document.body.appendChild(container);

            // Title
            let title = document.createElement('h1');
            title.innerText = `Ethics Report for ${ethicsReport.participant}`;
            container.appendChild(title);

            // Total score
            let totalScore = document.createElement('p');
            let ethicalStatus;
            if (ethicsReport.TotalScore <= 1) {
                ethicalStatus = "Completely Unethical";
                totalScore.classList.add("score-unethical");
            } else if (ethicsReport.TotalScore <= 2) {
                ethicalStatus = "Mostly Unethical";
                totalScore.classList.add("score-unethical");
            } else if (ethicsReport.TotalScore <= 3) {
                ethicalStatus = "Somewhat Unethical";
                totalScore.classList.add("score-unethical");
            } else if (ethicsReport.TotalScore <= 4) {
                ethicalStatus = "Mostly Ethical";
                totalScore.classList.add("score-ethical");
            } else {
                ethicalStatus = "Completely Ethical";
                totalScore.classList.add("score-ethical");
            }
            totalScore.innerText = `Total Score: ${ethicsReport.TotalScore.toFixed(2)} (${ethicalStatus})`;
            totalScore.classList.add('total-score');
            container.appendChild(totalScore);

            // Parameters
            for (let parameter of ethicsReport.Parameters) {
                let parameterElement = document.createElement('div');
                parameterElement.classList.add('parameter');
                container.appendChild(parameterElement);

                let parameterTitle = document.createElement('h2');
                parameterTitle.innerText = parameter.ParameterName;
                parameterElement.appendChild(parameterTitle);

                let parameterScore = document.createElement('h3');
                parameterScore.innerText = `Score: ${parameter.ParameterScore.toFixed(2)}`;
                parameterElement.appendChild(parameterScore);

                let parameterAnalysis = document.createElement('p');
                parameterAnalysis.innerText = parameter.ParameterAnalysis;
                parameterAnalysis.classList.add('analysis');
                parameterElement.appendChild(parameterAnalysis);

                // SubParameters
                for (let subParameter of parameter.SubParameters) {
                    let subParameterElement = document.createElement('div');
                    subParameterElement.classList.add('subparameter');
                    parameterElement.appendChild(subParameterElement);

                    let subParameterTitle = document.createElement('h4');
                    subParameterTitle.innerText = subParameter.SubParameterName;
                    subParameterElement.appendChild(subParameterTitle);

                    let subParameterScore = document.createElement('h5');
                    subParameterScore.innerText = `Score: ${subParameter.SubParameterScore.toFixed(2)}`;
                    subParameterElement.appendChild(subParameterScore);

                    let subParameterAnalysis = document.createElement('p');
                    subParameterAnalysis.innerText = subParameter.SubParameterAnalysis;
                    subParameterAnalysis.classList.add('analysis');
                    subParameterElement.appendChild(subParameterAnalysis);
                }
            }

            // Rules
            let rulesElement = document.createElement('h2');
            rulesElement.innerText = 'Rules:';
            container.appendChild(rulesElement);

            for (let rule of ethicsReport.Rules) {
                let ruleElement = document.createElement('p');
                ruleElement.innerText = rule;
                ruleElement.classList.add('rules');
                container.appendChild(ruleElement);
            }
        })
        .catch(error => console.error('Error:', error));
};
