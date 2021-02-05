graph [
  node [
    id 0
    label 1
    disk 5
    cpu 2
    memory 15
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 1
    memory 7
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 4
    memory 1
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 2
    memory 3
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 1
    memory 10
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 2
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 121
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 145
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 151
  ]
  edge [
    source 1
    target 3
    delay 34
    bw 126
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 154
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 162
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 66
  ]
]
