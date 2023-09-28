import argparse, textwrap

def my_logistic_regression(penalty, fit_intercept, max_iter, tol):
    from sklearn.linear_model import LogisticRegression

    #define a logistic regression object with your input params

    clf = LogisticRegression(penalty = penalty, fit_intercept = fit_intercept, max_iter = max_iter, tol = tol)

    print(clf)

parser = argparse.ArgumentParser(prog = "Logistic Regression",
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=textwrap.dedent('''\
                                        my_logistic_regression
                                     --------------------------------
                                     This program implements a regularized logistic regression.
                                     It requires four arguments:
                                                             
                                        1. penalty: (data type = string, default = 'l2') you can choose between 4 penalty options {'l1','l2','elasticnet','None'}
                                        2. fit_intercept: (data type = bool, default = True) specifies if a constant should be added {True, False}
                                        3. max_iter: (data type = int, default = 100) maximum number of iterations
                                        4. tol: (data type = float, default = 0.0001) tolerance from stopping criteria.   
                                                            '''),
                                epilog=textwrap.dedent('''\
                                     --------------------------------
                                        For a more detailed description of the arguments, please follow this link: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
                                     '''))


parser.add_argument('--penalty',default='l2', type=str, choices=['l1','l2','elasticnet','None'],
                    help ='You can only choose the following penalties: l1, l2, elasticnet, or None')
parser.add_argument('--fit_intercept', action='store_true', help='default value is given\
                    in the action property. If given, its value is True. True meaning an intercept/constant will be added, False otherwise.')
parser.add_argument('--max_iter', type = int, default = 100, help = 'maximum number of iterations') 
parser.add_argument('--tol', type = float, default = 0.0001, help = 'tolerance level from stopping')

args = parser.parse_args()
print(args)