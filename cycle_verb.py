cycle_verb_style = """
<style>
    .cycle-verb {
        display: inline-block;
    }
    
    .cycle-verb::before {
        display: inline-block;
        content: "";
        width: 5ch;
        text-align: center;
        animation: word-cycle 21s infinite, fade-cycle 7s infinite;

        @starting-style {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes word-cycle {
        0% {
            content: "like";
            font-weight: normal;
        }

        33% {
            content: "like";
        }

        34% {
            content: "adore";
        }

        66% {
            content: "adore";
            font-weight: normal;
        }

        67% {
            content: "love";
            font-weight: bold;
        }

        100% {
            content: "love";
            font-weight: bold;
        }
    }

    @keyframes fade-cycle {
        0% {
            opacity: 0;
            transform: translateY(-10%);
        }

        5% {
            opacity: 1;
            transform: translateY(0);
        }

        95% {
            opacity: 1;
            transform: translateY(0);
        }

        100% {
            opacity: 0;
            transform: translateY(10%);
        }
    }
</style>
"""

cycle_verb_element = """<div class="cycle-verb"></div>"""