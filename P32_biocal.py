import streamlit as st
from Bio.SeqUtils import molecular_weight, gc_fraction
from Bio.Seq import Seq

# App Configuration
st.set_page_config(page_title="BIOCAL", layout="wide")

# CSS Styling for colors and pointer cursor
st.markdown("""
    <style>
        a {
            text-decoration: none;
            color: blue;
            cursor: pointer;
        }
        .st-emotion-cache-1v0mbdj.ef3psqc4 {
            cursor: pointer;
        }
        .st-emotion-cache-1c7y2kd:hover {
            cursor: pointer !important;
        }
        .stSelectbox > div[role="button"] {
            cursor: pointer;
        }
        .orange-title {
            color: orange;
        }
        .orange-subheader {
            color: #FF8C00;
        }
        .stTabs [data-baseweb="tab"] button {
            color: blue !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Options
option = st.sidebar.selectbox("Select a function", (
    "Select a function",
    "Nucleotide Count & GC Content",
    "Molecular Weight Calculator",
    "Sequence Conversions",
    "DNA Length Utilities"
))

# Home Page
if option == "Select a function":
    st.header("Welcome to BIOCAL")
    st.markdown("""
        BioCal is a comprehensive toolkit designed to simplify molecular biology calculations,
        offering features like nucleotide count, GC content analysis, molecular weight estimation,
        sequence conversions, and DNA length utilities—all in one place.
    """)

    tab1, tab2, tab3 = st.tabs(["About Page", "Team Page", "Acknowledgement"])

    with tab1:
        st.subheader("About BIOCAL", help="Overview of the application")
        st.markdown("""
            <div class='orange-subheader'><strong>Overview</strong></div>
            BIOCAL is designed to assist in molecular biology calculations.

            <div class='orange-subheader'><strong>Objective</strong></div>
            To provide a one-stop platform for various common sequence-based and structural analyses.

            <div class='orange-subheader'><strong>Features</strong></div>
            - Nucleotide counting  
            - GC content analysis  
            - Molecular weight estimation  
            - DNA/RNA/Protein sequence conversions  
            - DNA and helix length utilities
        """, unsafe_allow_html=True)

    with tab2:
        st.subheader("Our Team", help="Details about contributors")
        st.markdown("<div class='orange-subheader'><strong>Contributor</strong></div>", unsafe_allow_html=True)
        cols = st.columns([0.2, 0.8])
        with cols[0]:
            st.image("Tejal photo.jpg", width=100)
        with cols[1]:
            st.markdown("**Tejal Takawale**")
        st.markdown("<div class='orange-subheader'><strong>Description</strong></div>", unsafe_allow_html=True)
        st.write("I am a MSc Bioinformatics student having interest in developing practical tools for researchers.")
        st.markdown("<div class='orange-subheader'><strong>Contact Information</strong></div>", unsafe_allow_html=True)
        st.write("Contact no. - 8767784471")
        st.write("Email - tejaltakawale09@gmail.com")

    with tab3:
        st.subheader("Acknowledgement")
        st.markdown("""
            I would like to express my heartfelt gratitude to all those who supported and guided me 
            throughout the course of this project. 

            I am especially thankful to **Dr. Kushagra Kashyap** and **Dr. Poonam Deshpande** for their 
            invaluable guidance, encouragement, and insightful suggestions, which played a significant role 
            in shaping the direction and quality of this work.

            I also extend my sincere appreciation to my colleagues for their cooperation, dedication, 
            and unwavering support during every stage of this project.
        """, unsafe_allow_html=True)

# Molecular Weight Calculator
elif option == "Molecular Weight Calculator":
    st.subheader("Molecular Weight Calculator")
    seq_input = st.text_area("Enter DNA/RNA/Protein sequence:", height=200)
    mol_type = st.radio("Select sequence type:", ["DNA", "RNA", "Protein"])

    if seq_input:
        seq = Seq(seq_input.replace("\n", "").upper())
        try:
            if mol_type == "DNA":
                weight = molecular_weight(seq, seq_type="DNA")
            elif mol_type == "RNA":
                weight = molecular_weight(seq, seq_type="RNA")
            else:
                weight = molecular_weight(seq, seq_type="protein")
            st.write(f"**Molecular Weight:** {weight:.2f} Da")
        except Exception as e:
            st.error("Error: " + str(e))

# Nucleotide Count & GC Content
elif option == "Nucleotide Count & GC Content":
    st.subheader("Nucleotide Count & GC Content")
    seq_input = st.text_area("Enter sequence:", height=200)

    if seq_input:
        seq = Seq(seq_input.replace("\n", "").upper())
        nucleotide_count = {n: seq.count(n) for n in "ACGT"}
        gc_content = gc_fraction(seq)

        st.write("**Nucleotide Counts:**")
        for nucleotide, count in nucleotide_count.items():
            st.write(f"{nucleotide}: {count}")

        st.write(f"**GC Content:** {gc_content:.2f}%")

# Sequence Conversions
elif option == "Sequence Conversions":
    st.subheader("Sequence Conversions")
    seq_input = st.text_area("Enter sequence:", height=200)
    conversion_type = st.radio("Select conversion type:", ["DNA to RNA", "RNA to DNA", "DNA to Protein", "RNA to Protein"])

    if seq_input:
        seq = Seq(seq_input.replace("\n", "").upper())
        if conversion_type == "DNA to RNA":
            st.write(f"**Converted Sequence (DNA to RNA):** {seq.transcribe()}")
        elif conversion_type == "RNA to DNA":
            st.write(f"**Converted Sequence (RNA to DNA):** {seq.back_transcribe()}")
        elif conversion_type == "DNA to Protein":
            st.write(f"**Converted Sequence (DNA to Protein):** {seq.translate()}")
        elif conversion_type == "RNA to Protein":
            st.write(f"**Converted Sequence (RNA to Protein):** {seq.translate()}")

# DNA Length Utilities
elif option == "DNA Length Utilities":
    st.header("Structural Calculation Tools")
    task = st.radio("Select what you have:", [
        "I have the number of amino acids (find helix length)",
        "I have the helix length (find number of amino acids)",
        "I have the number of base pairs (find DNA length)",
        "I have DNA length (find number of base pairs)"
    ])

    if task == "I have the number of amino acids (find helix length)":
        amino_acids = st.number_input("Enter the number of amino acids:", min_value=1, step=1)
        if amino_acids:
            helix_length = amino_acids * 0.34  # Example: 1 amino acid = 0.34 nm
            st.write(f"**Helix length:** {helix_length:.2f} nm")

    elif task == "I have the helix length (find number of amino acids)":
        helix_length = st.number_input("Enter the helix length (in nm):", min_value=0.1, step=0.1)
        if helix_length:
            amino_acids = helix_length / 0.34  # Example: 1 amino acid = 0.34 nm
            st.write(f"**Number of amino acids:** {amino_acids:.2f}")

    elif task == "I have the number of base pairs (find DNA length)":
        base_pairs = st.number_input("Enter the number of base pairs:", min_value=1, step=1)
        if base_pairs:
            dna_length = base_pairs * 0.34  # Example: 1 base pair = 0.34 nm
            st.write(f"**DNA length:** {dna_length:.2f} nm")

    elif task == "I have DNA length (find number of base pairs)":
        dna_length = st.number_input("Enter the DNA length (in nm):", min_value=0.1, step=0.1)
        if dna_length:
            base_pairs = dna_length / 0.34  # Example: 1 base pair = 0.34 nm
            st.write(f"**Number of base pairs:** {base_pairs:.2f}")
