from goldfarb_utils import test_df

t = test_df()
print(t.to_latex(formatters={'Man': lambda x: f'{x:.2%}'},
                 float_format='{:,.1f}'.format,
                 index_names=False,
                 column_format='lrr',
                 )
      )
