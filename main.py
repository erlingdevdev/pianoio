import mido


class Midi():
    def __init__(self):
        self.modtochord = {}
        self.chord_dict = self.chord_parser()
        
    def main(self):
        inp = mido.open_input()
        try:
            with mido.open_input() as port:
                for message in port:
                    inp = message
                    if inp.type == 'note_on':
                        x = (inp.note % 12) +1
                        print(x,inp.note, self.modtochord[x], message)
        except Exception:
            return 

    def chord_parser(self):
        d = {
       "C":[],
       "C#":[],
       "D":[],
       "D#":[],
       "E":[],
       "F":[],
       "F#":[],
       "G":[],
       "G#":[],
       "A":[],
       "A#":[],
       "B":[]
        }
        # key list
        lst = [key for key in d.keys()]

        # creates dictionary with every midi val corresponding to every note.
        for item, i  in enumerate(lst):
            for a in range(21,109):
                if a % 12 == item:
                    d[i].append(a)
            self.modtochord[int(item)+1] = i
        return d
if __name__ == "__main__":

    m = Midi()
    print(m.modtochord)

    m.main()


