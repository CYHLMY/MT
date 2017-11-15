def train_opts(parser):
    parser.add_argument("--data_file", default="data/hw5",
                        help="File prefix for training set.")
    parser.add_argument("--src_lang", default="words",
                        help="Source Language. (default = words)")
    parser.add_argument("--trg_lang", default="phoneme",
                        help="Target Language. (default = phoneme)")
    parser.add_argument("--model_file", default="test",
                        help="Location to dump the models.")
    parser.add_argument("--batch_size", default=48, type=int,
                        help="Batch size for training. (default=1)")
    parser.add_argument("--epochs", default=20, type=int,
                        help="Epochs through the data. (default=20)")
    parser.add_argument("--optimizer", default="Adam", choices=["SGD", "Adadelta", "Adam"],
                        help="Optimizer of choice for training. (default=Adam)")
    parser.add_argument("--learning_rate", "-lr", default=1e-3, type=float,
                        help="Learning rate of the optimization. (default=1e-3)")
    parser.add_argument("--momentum", default=0.9, type=float,
                        help="Momentum when performing SGD. (default=0.9)")
    parser.add_argument("--estop", default=1e-2, type=float,
                        help="Early stopping criteria on the development set. (default=1e-2)")
    parser.add_argument("--gpuid", default=[], nargs='+', type=int,
                        help="ID of gpu device to use. Empty implies cpu usage.")
    parser.add_argument("--show", default=1000, type=int,
                        help="show loss every ? batch default = 200")


def translation_opts(parser):
    parser.add_argument("--data_file", default="data/hw5",
                        help="File prefix for training set.")
    parser.add_argument("--src_lang", default="words",
                        help="Source Language. (default = words)")
    parser.add_argument("--trg_lang", default="phoneme",
                        help="Target Language. (default = phoneme)")
    parser.add_argument("--model_file", required=True,
                        help="Path of saved model.")
    parser.add_argument("--max_length", default=50, type=int, help="Max length of translated sentence")
