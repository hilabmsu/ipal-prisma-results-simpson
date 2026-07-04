from utils import load_data
from output import ensure_output_dirs
import sus
import ues
import ais
import ipq
import demographics

def main():
    ensure_output_dirs()
    df = load_data()

    sus.run(df)
    # ues.run(df)
    # ais.run(df)
    # ipq.run(df)
    # demographics.run(df)

if __name__ == '__main__':
    main()