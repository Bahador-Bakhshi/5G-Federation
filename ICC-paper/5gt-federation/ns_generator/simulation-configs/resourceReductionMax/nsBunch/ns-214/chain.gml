graph [
  node [
    id 0
    label 1
    disk 10
    cpu 2
    memory 10
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 1
    memory 10
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 3
    memory 2
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 1
    memory 14
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 2
    memory 6
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 2
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 172
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 147
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 171
  ]
  edge [
    source 1
    target 3
    delay 30
    bw 174
  ]
  edge [
    source 2
    target 5
    delay 34
    bw 154
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 103
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 153
  ]
]
