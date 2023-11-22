from gooey import Gooey, GooeyParser


def stress(a,b):
    a=float(a)
    b=float(b)
    c=a/b
    return c

def strain(a,b):
    a=float(a)
    b=float(b)
    c=a/b
    return c

def young(a,b):
    a=float(a)
    b=float(b)
    c=a/b
    return c

def poisson(a,b):
    a=float(a)
    b=float(b)
    c=a/b
    return c

def rigid(a,b):
    a=float(a)
    b=float(b)
    c=a/b
    return c

def volstrain(a,b):
    a=float(a)
    b=float(b)
    c=a/b
    return c

def bulk(a,b):
    a=float(a)
    b=float(b)
    c=a/b
    return c

@Gooey(navigation='TABBED', program_name="PyCalculator")
def main():
    parser = GooeyParser(description="To calculate various values such as Stress, Strain and the Elastic constants.")
    subparsers=parser.add_subparsers(required=True)

    Stress=subparsers.add_parser("Stress", help="To calculate Normal Stress")
    Stress.add_argument('--num1', help="Force applied in N",action="store" ,metavar="Force")
    Stress.add_argument('--num2', help="Area applied in mm²",metavar="Area",action="store")
    Stress.add_argument('--option1', help="click if using this tab", choices=["yes"],metavar="choose")
    

    Strain=subparsers.add_parser("Strain", help="To calculate Normal Strain")
    Strain.add_argument('--num3', help="Change in dimension",metavar="Delta",action="store")
    Strain.add_argument('--num4', help="Original Dimension",metavar="Original",action="store")
    Strain.add_argument('--option2', help="click if using this tab", choices=["yes"],metavar="choose")

    Young=subparsers.add_parser("Young", help="To calculate Young's Modulus")
    Young.add_argument('--num5', help="Stress in N/mm²",metavar="Stress",action="store")
    Young.add_argument('--num6', help="Strain",metavar='Strain',action="store")
    Young.add_argument('--option3', help="click if using this tab", choices=["yes"],metavar="choose")

    Poisson=subparsers.add_parser("Poisson", help="To calculate Poisson's Ratio")
    Poisson.add_argument('--num7', help="Lateral Strain",metavar="Lateral Strain",action="store")
    Poisson.add_argument('--num8', help="Liner Strain",metavar="Linear Strain",action="store")
    Poisson.add_argument('--option4', help="click if using this tab", choices=["yes"],metavar="choose")

    Rigid=subparsers.add_parser("Rigidity", help="To calculate Modulus of Rigidity")
    Rigid.add_argument('--num9', help="Shear Stress Applied in N/mm²",metavar="Shear Stress",action="store")
    Rigid.add_argument('--num10', help="Shear Strain",metavar="Shear Strain",action="store")
    Rigid.add_argument('--option5', help="click if using this tab", choices=["yes"],metavar="choose")

    Volstr=subparsers.add_parser("Vol", help="To calculate Volumentric strain")
    Volstr.add_argument('--num11', help="Change in Volume",metavar="Delta",action="store")
    Volstr.add_argument('--num112', help="Original Volume",metavar="Original",action="store")
    Volstr.add_argument('--option6', help="click if using this tab", choices=["yes"],metavar="choose")

    Bulk=subparsers.add_parser("Bulk", help="To calculate Bulk Modulus")
    Bulk.add_argument('--num13', help="Bulk Stress Applied in N/mm²",metavar="Bulk Stess",action="store")
    Bulk.add_argument('--num14', help="Bulk Strain",metavar="Bulk Strain",action="store")
    Bulk.add_argument('--option7', help="click if using this tab", choices=["yes"],metavar="choose")

    args = parser.parse_args()

    if "option1" in args:
        print(f"Stress= {stress(args.num1,args.num2)} N/mm²")
    if "option2" in args:
        print(f"Strain= {strain(args.num3,args.num4)} ")
    if "option3" in args:
        print(f"Young's Modulus= {young(args.num5,args.num6)} N/mm²")
    if "option4" in args:
        print(f"Poisson's Ratio= {poisson(args.num7,args.num8)} ")
    if "option5" in args:
        print(f"Modulus Of Rigidity= {rigid(args.num9,args.num10)} N/mm²")
    if "option6" in args:
        print(f"Volumetric Strain= {volstrain(args.num11,args.num12)} ")
    if "option7" in args:
        print(f"Bulk Modulus= {bulk(args.num13,args.num14)} N/mm²")
    
main()

