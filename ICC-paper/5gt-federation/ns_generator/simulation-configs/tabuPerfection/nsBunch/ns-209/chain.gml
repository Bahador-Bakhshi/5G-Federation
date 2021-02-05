graph [
  node [
    id 0
    label 1
    disk 8
    cpu 1
    memory 12
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 1
    memory 13
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 1
    memory 3
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 2
    memory 6
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 3
    memory 7
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 1
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 97
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 77
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 64
  ]
  edge [
    source 0
    target 3
    delay 26
    bw 63
  ]
  edge [
    source 1
    target 5
    delay 27
    bw 111
  ]
  edge [
    source 2
    target 5
    delay 35
    bw 189
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 125
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 115
  ]
]
