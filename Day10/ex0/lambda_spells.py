from typing import List


def artifact_sorter(artifacts: List[dict]) -> List[dict]:
    return sorted(artifacts, key=lambda items: items["power"], reverse=True)


def power_filter(mages: List[dict], min_power: int) -> List[dict]:
    return list(filter(lambda item: item['power'] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    return list(map(lambda nv: f"*{nv}*", spells))


def mage_stats(mages: list[dict]) -> dict:
    mx = max(mages, key=lambda x: x["power"])
    mi = min(mages, key=lambda x: x["power"])
    avg = round(sum(mage["power"] for mage in mages) / len(mages))

    return {"max_power": mx["power"],
            "min_power": mi["power"],
            "avg_power": avg
            }


def main() -> None:
    dictionnary = [{'name': "test", 'power': 3, 'element': "fire"},
                   {'name': "new", 'power': 55, 'element': "ice"},
                   {'name': "fires", 'power': 1, 'element': "sun"}]
    print()
    print("Resultat de arrtifact_sorter :", artifact_sorter(dictionnary))
    print()
    print("resultat de power_filter :", power_filter(dictionnary, 2))

    spell = ["Fire", "Ice", "92i"]
    print()
    print("Resultat de spell_tranformer :", spell_transformer(spell))
    print()
    print("Resultat de mage_stats:", mage_stats(dictionnary))


if __name__ == "__main__":
    main()
