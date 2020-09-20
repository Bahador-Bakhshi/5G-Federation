graph [
  node [
    id 0
    label 1
    disk 7
    cpu 1
    memory 14
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 4
    memory 14
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 1
    memory 1
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 4
    memory 9
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 2
    memory 7
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 1
    memory 5
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 109
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 129
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 147
  ]
  edge [
    source 0
    target 3
    delay 32
    bw 116
  ]
  edge [
    source 1
    target 4
    delay 33
    bw 50
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 82
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 154
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 50
  ]
]
