graph [
  node [
    id 0
    label 1
    disk 2
    cpu 2
    memory 2
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 2
    memory 2
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 2
    memory 9
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 3
    memory 13
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 2
    memory 3
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 3
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 189
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 97
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 117
  ]
  edge [
    source 2
    target 3
    delay 30
    bw 98
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 198
  ]
  edge [
    source 2
    target 5
    delay 31
    bw 144
  ]
]
