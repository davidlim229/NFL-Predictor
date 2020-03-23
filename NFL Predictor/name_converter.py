def get_team(name):
    name = name.lower()
    if name == 'ravens' or name == 'baltimore' or name == 'baltimore ravens' or name == 'bal':
        return 'RAV'
    if name == '49ers' or name == 'san francisco' or name == 'san francisco 49ers' or name == 'sf':
        return 'SFO'
    if name == 'buccaneers' or name == 'tampa bay' or name == 'tampa bay buccaneers' or name == 'tb':
        return 'TAM'
    if name == 'saints' or name == 'new orleans' or name == 'new orleans saints' or name == 'NO':
        return 'NOR'
    if name == 'chiefs' or name == 'kansas city' or name == 'kansas city chiefs' or name == 'kc':
        return 'KAN'
    if name == 'cowboys' or name == 'dallas' or name == 'dallas cowboys' or name == 'dal':
        return 'DAL'
    if name == 'patriots' or name == 'new england' or name == 'new england patriots' or name == 'ne':
        return 'NWE'
    if name == 'vikings' or name == 'minnesota' or name == 'minnesota vikings' or name == 'min':
        return 'MIN'
    if name == 'seahawks' or name == 'seattle' or name == 'seattle seahawks' or name == 'sea':
        return 'SEA'
    if name == 'titans' or name == 'tennessee' or name == 'tennessee titans' or name == 'ten':
        return 'OTI'
    if name == 'rams' or name == 'la rams' or name == 'los angeles rams' or name == 'st. louis rams' or name == 'lar' or name == 'stl' or name == 'st. louis':
        return 'RAM'
    if name == 'eagles' or name == 'philadelphia' or name == 'philadelphia eagles' or name == 'phi':
        return 'PHI'
    if name == 'falcons' or name == 'atlanta' or name == 'atlanta falcons' or name == 'atl':
        return 'ATL'
    if name == 'texans' or name == 'houston' or name == 'houston texans' or name == 'hou':
        return 'HTX'
    if name == 'packers' or name == 'green bay' or name == 'green bay packers' or name == 'gb':
        return 'GNB'
    if name == 'cardinals' or name == 'arizona' or name == 'arizona cardinals' or name == 'az':
        return 'CRD'
    if name == 'colts' or name == 'indianapolis' or name == 'indianapolis colts' or name == 'ind':
        return 'CLT'
    if name == 'lions' or name == 'detroit' or name == 'detroit lions' or name == 'det':
        return 'DET'
    if name == 'giants' or name == 'new york giants' or name == 'nyg':
        return 'NYG'
    if name == 'panthers' or name == 'carolina' or name == 'carolina panthers' or name == 'car':
        return 'CAR'
    if name == 'chargers' or name == 'la chargers' or name == 'los angeles chargers' or name == 'san diego chargers' or name == 'san diego' or name == 'lac' or name == 'sd':
        return 'SDG'
    if name == 'browns' or name == 'cleveland' or name == 'cleveland browns' or name == 'cle':
        return 'CLE'
    if name == 'bills' or name == 'buffalo' or name == 'buffalo bills' or name == 'buf':
        return 'BUF'
    if name == 'raiders' or name == 'las vegas' or name == 'oakland' or name == 'las vegas raiders' or name == 'oakland raiders' or name == 'lvr' or name == 'lv' or name == 'oak':
        return 'RAI'
    if name == 'dolphins' or name == 'miami' or name == 'miami dolphins' or name == 'mia':
        return 'MIA'
    if name == 'jaguars' or name == 'jacksonville' or name == 'jacksonville jaguars' or name == 'jax':
        return 'JAX'
    if name == 'steelers' or name == 'pittsburgh' or name == 'pittsburgh steelers' or name == 'pit':
        return 'PIT'
    if name == 'broncos' or name == 'denver' or name == 'denver broncos' or name == 'den':
        return 'DEN'
    if name == 'bears' or name == 'chicago' or name == 'chicago bears' or name == 'chi':
        return 'CHI'
    if name == 'bengals' or name == 'cincinnati' or name == 'cincinnati bengals' or name == 'cin':
        return 'CIN'
    if name == 'jets' or name == 'new york jets' or name == 'nyj':
        return 'NYJ'
    if name == 'redskins' or name == 'washington' or name == 'washington redskins' or name == 'was':
        return 'WAS'
    else:
        return None
