graph [
  node [
    id 0
    label 1
    disk 10
    cpu 2
    memory 9
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 4
    memory 6
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 4
    memory 11
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 4
    memory 6
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 1
    memory 6
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 3
    memory 7
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 186
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 125
  ]
  edge [
    source 1
    target 2
    delay 25
    bw 146
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 166
  ]
  edge [
    source 2
    target 4
    delay 34
    bw 91
  ]
  edge [
    source 2
    target 5
    delay 32
    bw 166
  ]
]
