# this is written as a list of tuples as 1 parameter in code A
# could map to 2 parameters in code B. Dictionaries are constructed below
eos_flavio_parameters = [
    ("GSW::sin^2(theta)", "s2w"),
    # ("CKM::A", "A"),
    # ("CKM::lambda", "laC"),
    # ("CKM::rhobar", "rhobar"),
    # ("CKM::etabar", "etabar"),
    ("QCD::alpha_s(MZ)", "alpha_s"),
    ("G_Fermi", "GF"),
    ("mass::e", "m_e"),
    ("mass::mu", "m_mu"),
    ("mass::tau", "m_tau"),
    ("mass::d(2GeV)", "m_d"),
    ("mass::s(2GeV)", "m_s"),
    ("mass::c", "m_c"),
    ("mass::b(MSbar)", "m_b"),
    ("mass::t(pole)", "m_t"),
    ("mass::pi^0", "m_pi0"),
    ("mass::pi^+", "m_pi+"),
    ("mass::K_d", "m_K0"),
    ("mass::K_u", "m_K+"),
    ("mass::K^*_d", "m_K*0"),
    ("mass::K^*_u", "m_K*+"),
    ("mass::D^+", "m_D+"),
    ("mass::D^0", "m_D0"),
    ("mass::B_d", "m_B0"),
    ("mass::B_u", "m_B+"),
    ("mass::B_s", "m_Bs"),
    ("mass::Lambda", "m_Lambda"),
    ("mass::Lambda_b", "m_Lambdab"),
    ("mass::W", "m_W"),
    ("mass::Z", "m_Z"),
    ("decay-constant::B_d", "f_B0"),
    ("decay-constant::B_u", "f_B+"),
    ("decay-constant::B_s", "f_Bs"),
    ("decay-constant::K_d", "f_K0"),
    ("decay-constant::K_u", "f_K+"),
    ("decay-constant::pi", "f_pi+"),
    # ("life_time::B_d", "tau_B0"),
    # ("life_time::B_u", "tau_B+"),
    # ("life_time::B_s", "tau_Bs"),
    # ("life_time::Lambda_b", "tau_Lambdab"),
    ("Lambda::alpha", "Lambda->ppi alpha_-"),
    ("Lambda_b->Lambda::a_0_time^V@DM2016", "Lambdab->Lambda SSE a0_fVt"),
    ("Lambda_b->Lambda::a_1_time^V@DM2016", "Lambdab->Lambda SSE a1_fVt"),
    ("Lambda_b->Lambda::a_2_time^V@DM2016", "Lambdab->Lambda SSE a2_fVt"),
    ("Lambda_b->Lambda::a_0_time^A@DM2016", "Lambdab->Lambda SSE a0_fAt"),
    ("Lambda_b->Lambda::a_1_time^A@DM2016", "Lambdab->Lambda SSE a1_fAt"),
    ("Lambda_b->Lambda::a_2_time^A@DM2016", "Lambdab->Lambda SSE a2_fAt"),
    ("Lambda_b->Lambda::a_0_long^V@DM2016", "Lambdab->Lambda SSE a0_fV0"),
    ("Lambda_b->Lambda::a_1_long^V@DM2016", "Lambdab->Lambda SSE a1_fV0"),
    ("Lambda_b->Lambda::a_2_long^V@DM2016", "Lambdab->Lambda SSE a2_fV0"),
    ("Lambda_b->Lambda::a_0_perp^V@DM2016", "Lambdab->Lambda SSE a0_fVperp"),
    ("Lambda_b->Lambda::a_1_perp^V@DM2016", "Lambdab->Lambda SSE a1_fAperp"),
    ("Lambda_b->Lambda::a_2_perp^V@DM2016", "Lambdab->Lambda SSE a2_fAperp"),
    ("Lambda_b->Lambda::a_0_long^A@DM2016", "Lambdab->Lambda SSE a0_fA0"),
    ("Lambda_b->Lambda::a_1_long^A@DM2016", "Lambdab->Lambda SSE a1_fA0"),
    ("Lambda_b->Lambda::a_2_long^A@DM2016", "Lambdab->Lambda SSE a2_fA0"),
    ("Lambda_b->Lambda::a_1_perp^A@DM2016", "Lambdab->Lambda SSE a1_fAperp"),
    ("Lambda_b->Lambda::a_2_perp^A@DM2016", "Lambdab->Lambda SSE a2_fAperp"),
    ("Lambda_b->Lambda::a_0_long^T@DM2016", "Lambdab->Lambda SSE a0_fT0"),
    ("Lambda_b->Lambda::a_1_long^T@DM2016", "Lambdab->Lambda SSE a1_fT0"),
    ("Lambda_b->Lambda::a_2_long^T@DM2016", "Lambdab->Lambda SSE a2_fT0"),
    ("Lambda_b->Lambda::a_0_perp^T@DM2016", "Lambdab->Lambda SSE a0_fTperp"),
    ("Lambda_b->Lambda::a_1_perp^T@DM2016", "Lambdab->Lambda SSE a1_fTperp"),
    ("Lambda_b->Lambda::a_2_perp^T@DM2016", "Lambdab->Lambda SSE a2_fTperp"),
    ("Lambda_b->Lambda::a_0_long^T5@DM2016", "Lambdab->Lambda SSE a0_fT50"),
    ("Lambda_b->Lambda::a_1_long^T5@DM2016", "Lambdab->Lambda SSE a1_fT50"),
    ("Lambda_b->Lambda::a_2_long^T5@DM2016", "Lambdab->Lambda SSE a2_fT50"),
    ("Lambda_b->Lambda::a_1_perp^T5@DM2016", "Lambdab->Lambda SSE a1_fT5perp"),
    ("Lambda_b->Lambda::a_2_perp^T5@DM2016", "Lambdab->Lambda SSE a2_fT5perp"),
    # ("B->K^*::alpha^A0_0@BSZ2015", "B->K* BSZ a0_A0"),
    ("B->K^*::alpha^A0_1@BSZ2015", "B->K* BSZ a1_A0"),
    ("B->K^*::alpha^A0_2@BSZ2015", "B->K* BSZ a2_A0"),
    ("B->K^*::alpha^A1_0@BSZ2015", "B->K* BSZ a0_A1"),
    ("B->K^*::alpha^A1_1@BSZ2015", "B->K* BSZ a1_A1"),
    ("B->K^*::alpha^A1_2@BSZ2015", "B->K* BSZ a2_A1"),
    ("B->K^*::alpha^A12_1@BSZ2015", "B->K* BSZ a1_A12"),
    ("B->K^*::alpha^A12_2@BSZ2015", "B->K* BSZ a2_A12"),
    ("B->K^*::alpha^V_0@BSZ2015", "B->K* BSZ a0_V"),
    ("B->K^*::alpha^V_1@BSZ2015", "B->K* BSZ a1_V"),
    ("B->K^*::alpha^V_2@BSZ2015", "B->K* BSZ a2_V"),
    ("B->K^*::alpha^T1_0@BSZ2015", "B->K* BSZ a0_T1"),
    ("B->K^*::alpha^T1_1@BSZ2015", "B->K* BSZ a2_T1"),
    ("B->K^*::alpha^T1_2@BSZ2015", "B->K* BSZ a2_T1"),
    ("B->K^*::alpha^T2_1@BSZ2015", "B->K* BSZ a1_T2"),
    ("B->K^*::alpha^T2_2@BSZ2015", "B->K* BSZ a2_T2"),
    ("B->K^*::alpha^T23_0@BSZ2015", "B->K* BSZ a0_T23"),
    ("B->K^*::alpha^T23_1@BSZ2015", "B->K* BSZ a1_T23"),
    ("B->K^*::alpha^T23_2@BSZ2015", "B->K* BSZ a2_T23"),
    ("B->K^*::f_Kstar_par", "f_K*0"),
    ("B->K^*::f_Kstar_perp@2GeV", "f_perp_K*0"),
    ("B->K^*::f_Kstar_par", "f_K*+"),
    ("B->K^*::f_Kstar_perp@2GeV", "f_perp_K*+"),
    ("exp::BR(B->X_clnu)", "BR(B->Xcenu)_exp"),
    ("exp::C(B->X_clnu, B->X_ulnu)", "C_BXlnu"),
]

# dictionaries
dict_eos2flavio = {e: f for e, f in eos_flavio_parameters}
dict_flavio2eos = {f: e for e, f in eos_flavio_parameters}
