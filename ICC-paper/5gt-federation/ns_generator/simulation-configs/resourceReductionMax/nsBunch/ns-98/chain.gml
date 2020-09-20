graph [
  node [
    id 0
    label 1
    disk 7
    cpu 2
    memory 1
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 1
    memory 9
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 4
    memory 15
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 3
    memory 7
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 3
    memory 14
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 4
    memory 5
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 152
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 138
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 70
  ]
  edge [
    source 2
    target 3
    delay 31
    bw 174
  ]
  edge [
    source 2
    target 4
    delay 34
    bw 114
  ]
  edge [
    source 2
    target 5
    delay 27
    bw 154
  ]
]
