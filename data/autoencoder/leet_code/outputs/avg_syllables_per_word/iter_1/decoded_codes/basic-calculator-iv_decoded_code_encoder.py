from collections import defaultdict
import re

class Term:
    def __init__(self, coef, vars):
        self.coef = coef
        self.vars = tuple(sorted(vars))

    def __hash__(self):
        return hash(self.vars)

    def __eq__(self, other):
        return self.vars == other.vars

    def __lt__(self, other):
        # sort terms by length desc, then lex order
        if len(self.vars) != len(other.vars):
            return len(self.vars) > len(other.vars)
        return self.vars < other.vars

    def __str__(self):
        if not self.vars:
            return str(self.coef)
        return str(self.coef) + "*" + "*".join(self.vars)

class Expression:
    def __init__(self, terms=None):
        # terms is dict Term -> coef
        self.terms = defaultdict(int)
        if terms:
            for t in terms:
                self.terms[t] += t.coef
        self.clean()

    @classmethod
    def from_term(cls, term):
        expr = cls()
        expr.terms[Term(term.coef, term.vars)] = 1
        expr.clean()
        return expr

    def clean(self):
        # remove zero coef terms
        self.terms = defaultdict(int, {t: c for t,c in self.terms.items() if c != 0})

    def add(self, other):
        res = Expression()
        for t,c in self.terms.items():
            res.terms[t] += c
        for t,c in other.terms.items():
            res.terms[t] += c
        res.clean()
        return res

    def subtract(self, other):
        res = Expression()
        for t,c in self.terms.items():
            res.terms[t] += c
        for t,c in other.terms.items():
            res.terms[t] -= c
        res.clean()
        return res

    def multiply(self, other):
        res = Expression()
        for t1,c1 in self.terms.items():
            for t2,c2 in other.terms.items():
                coef = c1 * c2
                vars = sorted(t1.vars + t2.vars)
                res.terms[Term(coef, vars)] += coef
        res.clean()
        return res

    def to_list(self):
        # sort terms: length vars desc, lex order vars asc
        # output format: ["coef*var1*var2", "coef"]
        terms = list(self.terms.items())
        terms = [(t, c) for t,c in self.terms.items()]
        # Combine coef into Term.coef because keys' coef unused (0 or 1)
        # Actually we stored coef in key.coef and counts in value - incorrect.
        # We stored coef in both places incorrectly. Fixing scheme:
        # We should treat Term.vars as key, coef in dict value.
        # So let's redefine Expression to store terms as dict: vars tuple -> coef.
        pass

def parse_expression(expression, evalvars, evalints):
    var_map = {v:k for v,k in zip(evalvars, evalints)}  # var -> int coef

    # Fix Expression and Term design: We keep vars tuple as key and coef in dict value

class Term:
    def __init__(self, coef, vars):
        self.coef = coef
        self.vars = tuple(sorted(vars))
    def __hash__(self):
        return hash(self.vars)
    def __eq__(self, other):
        return self.vars == other.vars
    def __lt__(self, other):
        if len(self.vars)!=len(other.vars): return len(self.vars) > len(other.vars)
        return self.vars < other.vars
    def __str__(self):
        if not self.vars: return str(self.coef)
        return str(self.coef) + "*" + "*".join(self.vars)

class Expression:
    def __init__(self, terms=None):
        # terms: dict vars tuple -> coef
        self.terms = defaultdict(int)
        if terms:
            for vars_, coef in terms.items():
                self.terms[vars_] += coef
        self.clean()
    @classmethod
    def from_term(cls, term):
        return cls({term.vars: term.coef})
    def clean(self):
        self.terms = defaultdict(int, {k:v for k,v in self.terms.items() if v!=0})
    def add(self, other):
        res = Expression()
        for var, coef in self.terms.items():
            res.terms[var] += coef
        for var, coef in other.terms.items():
            res.terms[var] += coef
        res.clean()
        return res
    def subtract(self, other):
        res = Expression()
        for var, coef in self.terms.items():
            res.terms[var] += coef
        for var, coef in other.terms.items():
            res.terms[var] -= coef
        res.clean()
        return res
    def multiply(self, other):
        res = Expression()
        for v1, c1 in self.terms.items():
            for v2, c2 in other.terms.items():
                vars_ = tuple(sorted(v1 + v2))
                res.terms[vars_] += c1 * c2
        res.clean()
        return res
    def to_list(self):
        # sort terms by length desc, lexical order asc
        terms = sorted(self.terms.items(), key=lambda x: (-len(x[0]), x[0]))
        result = []
        for vars_, coef in terms:
            if coef == 0:
                continue
            if not vars_:
                result.append(str(coef))
            else:
                result.append(str(coef) + "*" + "*".join(vars_))
        return result

def tokenize(expression):
    # tokenize by spaces and operators/parens
    tokens = []
    i = 0
    while i < len(expression):
        c = expression[i]
        if c == ' ':
            i += 1
            continue
        if c in '()+-*':
            tokens.append(c)
            i += 1
        else:
            j = i
            while j < len(expression) and (expression[j].isalnum()):
                j += 1
            tokens.append(expression[i:j])
            i = j
    return tokens

def parse(expression, evalvars, evalints):
    var_map = dict(zip(evalvars, evalints))
    tokens = tokenize(expression)

    output = []
    operators = []

    def apply_operator():
        r = output.pop()
        l = output.pop()
        op = operators.pop()
        if op == '+':
            output.append(l.add(r))
        elif op == '-':
            output.append(l.subtract(r))
        elif op == '*':
            output.append(l.multiply(r))

    for token in tokens:
        if token.isdigit():
            output.append(Expression.from_term(Term(int(token), ())))
        elif token.isalpha():
            coef = var_map.get(token, 1)
            if coef == 1:
                output.append(Expression.from_term(Term(1, (token,))))
            else:
                # number replacement treated as constant term
                output.append(Expression.from_term(Term(coef, ())))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator()
            operators.pop() # remove '('
        else: # operator + - *
            while operators and operators[-1] != '(' and (token in '+-' or operators[-1] == '*'):
                apply_operator()
            operators.append(token)

    while operators:
        apply_operator()

    return output[0].to_list()