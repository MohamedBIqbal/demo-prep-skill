#!/bin/bash
# Terminal Demo Script Template
# Run: ./demo.sh           # Full demo
# Run: ./demo.sh 1         # Section 1 only
# Run: ./demo.sh 1 2 3     # Sections 1, 2, 3
# Sections: 0=title, 1=hook, 2=solution, 3=demo, 4=results, 5=next, 6=ask

set -e
cd "$(dirname "$0")"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

pause() {
    echo ""
    read -p "Press Enter to continue..."
    clear
}

header() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}$1${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

# Optional: Check if server is running (uncomment and modify for your API)
# check_server() {
#     echo -e "${YELLOW}Checking server...${NC}"
#     if ! curl -s http://localhost:8000/health > /dev/null 2>&1; then
#         echo "Server not running. Start with: your-server-command"
#         exit 1
#     fi
#     echo -e "${GREEN}✓ Server is healthy${NC}"
#     sleep 1
#     clear
# }

# ============================================================================
# SECTION 0: TITLE CARD
# ============================================================================
section_0_title() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}     ██████╗ ███████╗███╗   ███╗ ██████╗ ${NC}"
    echo -e "${GREEN}     ██╔══██╗██╔════╝████╗ ████║██╔═══██╗${NC}"
    echo -e "${GREEN}     ██║  ██║█████╗  ██╔████╔██║██║   ██║${NC}"
    echo -e "${GREEN}     ██║  ██║██╔══╝  ██║╚██╔╝██║██║   ██║${NC}"
    echo -e "${GREEN}     ██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝${NC}"
    echo -e "${GREEN}     ╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ${NC}"
    echo -e "${YELLOW}          Your Product Tagline Here${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    pause
}

# ============================================================================
# SECTION 1: HOOK + PROBLEM (1 min)
# ============================================================================
section_1_hook() {
    header "THE PROBLEM"

    echo -e "${YELLOW}[Your opening hook - why should they care?]${NC}"
    echo ""
    echo "Key pain points:"
    echo -e "  ${CYAN}→${NC} Pain point 1"
    echo -e "  ${CYAN}→${NC} Pain point 2"
    echo -e "  ${CYAN}→${NC} Pain point 3"
    echo ""
    echo -e "${RED}The challenge:${NC}"
    echo ""
    echo "  ┌──────────────────────────┬─────────────────────────┐"
    echo "  │ Category                 │ Impact                  │"
    echo "  ├──────────────────────────┼─────────────────────────┤"
    echo "  │ Example metric 1         │ Value                   │"
    echo "  │ Example metric 2         │ Value                   │"
    echo "  │ Example metric 3         │ Value                   │"
    echo "  └──────────────────────────┴─────────────────────────┘"
    echo ""

    # Optional: Dynamic data from API
    # curl -s "http://localhost:8000/your-endpoint" | python3 -c "
    # import sys, json
    # data = json.load(sys.stdin)
    # # Format and print your data
    # "

    echo -e "${GREEN}Your product addresses these concerns.${NC}"
    pause
}

# ============================================================================
# SECTION 2: SOLUTION OVERVIEW (30 sec)
# ============================================================================
section_2_solution() {
    header "THE SOLUTION"

    echo -e "${GREEN}Key components of your solution:${NC}"
    echo ""
    echo -e "  ${CYAN}1. Component 1${NC}     Description"
    echo -e "  ${CYAN}2. Component 2${NC}     Description"
    echo -e "  ${CYAN}3. Component 3${NC}     Description"
    echo -e "  ${CYAN}4. Component 4${NC}     Description"
    echo ""
    echo -e "${YELLOW}Architecture:${NC}"
    echo ""
    echo "  Input → [Your Process] → Output"
    echo "              ↓"
    echo "        [Verification]"
    echo "              ↓"
    echo "         [Result]"
    pause
}

# ============================================================================
# SECTION 3: LIVE DEMO (2 min)
# ============================================================================
section_3_demo() {
    header "LIVE DEMO: Part 1"

    echo -e "${YELLOW}Scenario:${NC} Describe what you're about to show"
    echo ""

    # Example: API call demo
    # curl -s -X POST http://localhost:8000/your-endpoint \
    #   -H "Content-Type: application/json" \
    #   -d '{"key": "value"}' \
    #   | python3 -c "
    # import sys, json
    # data = json.load(sys.stdin)
    # print('Result:', data.get('result'))
    # "

    echo "=== DEMO OUTPUT ==="
    echo "[Your demo output would appear here]"
    echo ""
    echo "Key observations:"
    echo "  • Observation 1"
    echo "  • Observation 2"
    echo "  • Observation 3"

    pause

    header "LIVE DEMO: Part 2 - Edge Case"

    echo -e "${YELLOW}Scenario:${NC} Show how you handle edge cases"
    echo ""
    echo "=== INPUT ==="
    echo "[Edge case input]"
    echo ""
    echo -e "${RED}=== HANDLING ===${NC}"
    echo ""
    echo "[Show how your system handles the edge case]"
    pause
}

# ============================================================================
# SECTION 4: RESULTS (30 sec)
# ============================================================================
section_4_results() {
    header "RESULTS"

    echo -e "${GREEN}Validation:${NC}"
    echo "  • Metric 1: Value"
    echo "  • Metric 2: Value"
    echo "  • Metric 3: Value"
    echo ""
    echo -e "${GREEN}Performance:${NC}"
    echo "  • Benchmark 1: Result"
    echo "  • Benchmark 2: Result"
    echo "  • Benchmark 3: Result"
    pause
}

# ============================================================================
# SECTION 5: CHALLENGES + NEXT STEPS (30 sec)
# ============================================================================
section_5_next() {
    header "CHALLENGES & NEXT STEPS"

    echo -e "${YELLOW}Current Challenges:${NC}"
    echo "  • Challenge 1"
    echo "  • Challenge 2"
    echo "  • Challenge 3"
    echo ""
    echo -e "${GREEN}Roadmap:${NC}"
    echo "  1. Next milestone"
    echo "  2. Following milestone"
    echo "  3. Future goal"
    echo ""
    echo -e "${GREEN}Vision:${NC}"
    echo "  [Your long-term vision statement]"
    pause
}

# ============================================================================
# SECTION 6: THE ASK (30 sec)
# ============================================================================
section_6_ask() {
    header "THE ASK"

    echo -e "${GREEN}Vision:${NC}"
    echo "  [Restate your vision in one sentence]"
    echo ""
    echo -e "${YELLOW}What I need:${NC}"
    echo ""
    echo "  1. ${CYAN}Feedback/Advice${NC}"
    echo "     Specific question or area"
    echo ""
    echo "  2. ${CYAN}Connections/Introductions${NC}"
    echo "     Who would be valuable to connect with?"
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}Thank you!${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

# ============================================================================
# MAIN
# ============================================================================

# Optional: Uncomment to check server before demo
# check_server

# If no arguments, run all sections
if [ $# -eq 0 ]; then
    section_0_title
    section_1_hook
    section_2_solution
    section_3_demo
    section_4_results
    section_5_next
    section_6_ask
    exit 0
fi

# Run specified sections
for section in "$@"; do
    case $section in
        0|title)    section_0_title ;;
        1|hook)     section_1_hook ;;
        2|solution) section_2_solution ;;
        3|demo)     section_3_demo ;;
        4|results)  section_4_results ;;
        5|next)     section_5_next ;;
        6|ask)      section_6_ask ;;
        *)
            echo "Unknown section: $section"
            echo "Usage: ./demo.sh [0-6...]"
            echo "  0|title    - Title card"
            echo "  1|hook     - Problem statement"
            echo "  2|solution - Solution components"
            echo "  3|demo     - Live demo"
            echo "  4|results  - Results + metrics"
            echo "  5|next     - Challenges & roadmap"
            echo "  6|ask      - The ask"
            exit 1
            ;;
    esac
done
