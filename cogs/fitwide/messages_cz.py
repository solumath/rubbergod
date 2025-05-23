from config.messages import Messages as GlobalMessages


class MessagesCZ(GlobalMessages):
    increment_roles_brief = "Aktualizuje role na serveru podle ročníku. Aktualizace školních roomek."
    increment_roles_start = "Incrementing roles..."
    increment_roles_names = "1/3 - Role úspěšně přejmenovány a 0bit a 0mit vytvořen"
    increment_roles_room_names = "2/3 - Kanály úspěšně přejmenovány a 0bit a 0mit general vytvořen"
    increment_roles_success = "3/3 - Holy fuck, všechno se povedlo, tak zase za rok <:Cauec:602052606210211850>"
    verify_check_brief = "Zkontroluje uživatelům s verify rolí zda jsou v databázi"
    verify_check_user_not_found = "Ve verified databázi jsem nenašel: {user} ({id})"
    status_check_brief = "Zkontroluje uživatelům jestli stav jejich loginu v databázi je \"použit\""
    status_check_user_duplicate = "{user} ({id}) je v permit databázi víckrát?"
    status_check_wrong_status = "Status nesedí u: {user} ({id})"
    zapis_check_brief = "Zkontroluje ročníkové role uživatelům, jestli se nezapoměli zapsat do dalšího ročníku"
    zapis_check_found = "Vypadá, že do dalšího ročníku se nezapsali (protoze v API maji {target_year}): "
    mit_check_brief = "Zkontroluje uživatele, jestli se nezapsali na MIT studium"
    exstudent_check_brief = "zkontroluje uživatelům, jestli nedropnuli"
    role_check_brief = "zkontroluje ročníkové role uživatelům"
    role_check_start = "Kontrola uživatelů ..."
    role_check_end = "Hotovo"
    role_check_found = "Našel jsem {people_count} lidi, kteří mají v API {target_year} ale roli {source_year}:"
    role_check_move = "Přesouvám tyto {people_count} lidi z {source_year} do {target_year}:"
    role_check_debug_mode = "jk, debug mode"
    fitwide_brief = "Příkazy na manipulaci verify studentů"
    update_db_brief = "Aktualizuje databázi s loginy"
    update_db_continue_from_login = "Pokračovat v aktualizaci databáze od loginu (včetně)"
    update_db_start = "Aktualizuji databázi..."
    update_db_progress = "Progress: {progress_bar}."
    update_db_done = "Aktualizace databáze proběhla úspěšně. Nalezeno {exstudent_count} nových ExStudent."
    update_db_single_brief = "Aktualizuje data pro login"
    update_db_single_login = "Login který aktualizovat"
    update_db_single_no_login = "Nebyl zadán login"
    update_db_single_done = "Aktualizace databáze uživatele proběhla úspěšně."
    update_db_not_in_db = "Uživatel není v db"
    pull_db_brief = "Stáhne databázi uživatelů na merlinovi"
    get_db_error = "Při stahování databáze došlo k chybě."
    get_db_timeout = "Timeout při stahování databáze."
    get_db_success = "Stažení databáze proběhlo úspěšně."
    get_login_brief = "Získá xlogin uživatele"
    login_not_found = "Uživatel není v databázi."
    getting_info_from_api = "Získávám informace o uživateli z VUT API..."
    get_user_brief = "Získá discord uživatele"
    get_user_not_found = "Uživatel není v databázi možných loginů."
    get_user_format = "Login: `{p.login}`\nJméno: `{p.name}`\n" "Ročník: `{p.year}`\n"
    invalid_login = "Toto není validní login."
    action_success = "Příkaz proběhl úspěšně."
    reset_login_brief = "Odstraní uživatele z verify databáze"
    link_login_user_brief = "Propojí login s uživatelem"
    link_login_prompt = "Opravdu chceš propojit login `{login}` s uživatelem {user}, i když není v API?"
    not_in_modroom = "Nothing to see here comrade. <:KKomrade:484470873001164817>"
    login_already_exists = "Uživatel již existuje v databázi."
    vutapi_brief = "Získá data z VUT API"
    gen_teacher_info_brief = "Generuje informace o vyučujících"
    gen_teacher_info_start = "Generuji informace o vyučujících..."
    gen_teacher_info_header = "# Vyučující v předmětových kanálech"
    gen_teacher_info_processing = "Generuji informace o vyučujících: {progress_bar}"
    gen_teacher_info_success = "Informace o vyučujících byly úspěšně vygenerovány."
    gen_teacher_info_inv_catg = "Některé kategorie mají neplatné názvy. Hodilo by se je opravit: {categories}"
    gen_teacher_info_inv_roles = "Nemohu najít role pro vyučující."
    gen_teacher_info_channel_none = "Nemohu najít kanál vyucujici-info."
