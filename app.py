# -*- coding:utf-8 -*-
import streamlit as st
from eda_app import run_eda_app
from ml_app import run_ml_app

def main():
    st.markdown("Iris Research")
    menu = ["Home", "Exclusive Information", "Research","Machine Learned Data", "About Us"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.title("Iris (Plant)")
        st.text("We are a website that exclusively deals information about Iris.") 
        st.text("For more information click the arrow on the top left corner.")
        image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Iris_germanica_%28Purple_bearded_Iris%29%2C_Wakehurst_Place%2C_UK_-_Diliff.jpg/220px-Iris_germanica_%28Purple_bearded_Iris%29%2C_Wakehurst_Place%2C_UK_-_Diliff.jpg"
        st.image(image_url, caption="A Beautiful Image of an Iris")
        
    elif choice == "Exclusive Information":
        st.title("Definiton")
        st.text("Iris is a flowering plant genus of 310 accepted species with showy flowers. \nAs well as being the scientific name, iris is also widely used as a common \nname for all Iris species, as well as some belonging to other closely \nrelated genera. A common name for some species is flags, while the plants \nof the subgenus Scorpiris are widely known as junos, particularly in \nhorticulture. It is a popular garden flower. The often-segregated, monotypic\ngenera Belamcanda (blackberry lily, I. domestica), \nHermodactylus (snake's head iris, I. tuberosa), and \nPardanthopsis (vesper iris, I. dichotoma) are currently included in Iris. \nThree Iris varieties are used in the Iris flower data set outlined by Ronald \nFisher in his 1936 paper The use of multiple measurements in taxonomic \nproblems as an example of linear discriminant analysis.")
        with st.expander("Taxonomy"):
             st.write("It takes its name from the Greek word ἶρις îris \"rainbow\", which is \nalso the name for the Greek goddess of the rainbow, Iris. Some authors state\nthat the name refers to the wide variety of flower colors found among \nthe many species. Iris is the largest genus of the family Iridaceae with up \nto 300 species – many of them natural hybrids. Plants of the World \nOnline lists 310 accepted species from this genus as of 2022.Modern classifications, starting \nwith Dykes (1913), have subdivided them. Dykes referred \nto the major subgroupings as sections. Subsequent authors such as \nLawrence (1953) and Rodionenko (1987) have generally called them \nsubgenera, while essentially retaining Dykes' groupings, using \nsix subgenera further divided into twelve sections. Of these, \nsection Limneris (subgenus Limneris) was further divided \ninto sixteen series. Like some older sources, Rodionenko moved some of the bulbous \nsubgenera (Xiphium, Scorpiris and Hermodactyloides) into separate genera \n(Xiphion, Juno and Iridodictyum respectively), but this has not been accepted by later writers such as Mathew (1989), \nalthough the latter kept Hermodactylus as a distinct genus, to include Hermodactylus tuberosus, \nnow returned to Hermodactyloides as Iris tuberosa. Rodionenko also reduced the \nnumber of sections in subgenus Iris, from six to two, depending on the \npresence (Hexapogon) or absence (Iris) of arils on the seeds, referred to as arilate \nor nonarilate. Taylor (1976) provides arguments for not including all \narilate species in Hexapogon. In general, modern classifications usually recognise six \nsubgenera, of which five are restricted to the Old World; the sixth \n(subgenus Limniris) has a Holarctic distribution. The two largest subgenera \nare further divided into sections. The Iris subgenus has been divided \ninto six sections; bearded irises (or pogon irises), \nPsammiris, Oncocyclus, Regelia, Hexapogon and Pseudoregelia. \nIris subg. Limniris has been divided into 2 sections; Lophiris \n(or 'Evansias' or crested iris) and Limniris which was \nfurther divided into 16 series.")
        with st.expander("Description"):
             st.write("Irises are perennial plants, growing from creeping rhizomes \n(rhizomatous irises) or, in drier climates, from bulbs (bulbous irises). \nThey have long, erect flowering stems which may be simple or branched, \nsolid or hollow, and flattened or have a circular cross-section. \nThe rhizomatous species usually have 3–10 basal sword-shaped leaves growing in dense \nclumps. The bulbous species also have 2–10 narrow leaves growing from the bulb.")
    elif choice == "Research":
        run_eda_app()
    elif choice == "Machine Learned Data":
        run_ml_app()
    else:
        st.subheader("About Us")
        st.video("https://www.youtube.com/watch?v=GcrBR-cqD0k&ab_channel=NeilBromhall")
        st.text("We are a research team trying to spread the beauty of the flower called Iris.")
        

if __name__ == "__main__":
    main()