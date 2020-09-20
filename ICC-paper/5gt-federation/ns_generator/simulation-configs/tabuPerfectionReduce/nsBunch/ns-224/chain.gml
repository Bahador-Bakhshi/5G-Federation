graph [
  node [
    id 0
    label 1
    disk 2
    cpu 1
    memory 9
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 3
    memory 7
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 2
    memory 7
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 4
    memory 9
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 1
    memory 8
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 1
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 185
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 107
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 173
  ]
  edge [
    source 0
    target 3
    delay 34
    bw 129
  ]
  edge [
    source 1
    target 4
    delay 34
    bw 194
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 188
  ]
  edge [
    source 3
    target 5
    delay 26
    bw 59
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 54
  ]
]
