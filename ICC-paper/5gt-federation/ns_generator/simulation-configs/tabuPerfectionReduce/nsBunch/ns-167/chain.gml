graph [
  node [
    id 0
    label 1
    disk 5
    cpu 3
    memory 11
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 4
    memory 16
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 1
    memory 5
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 2
    memory 2
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 2
    memory 2
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 2
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 193
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 146
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 112
  ]
  edge [
    source 2
    target 3
    delay 26
    bw 162
  ]
  edge [
    source 2
    target 4
    delay 27
    bw 151
  ]
  edge [
    source 2
    target 5
    delay 34
    bw 193
  ]
]
