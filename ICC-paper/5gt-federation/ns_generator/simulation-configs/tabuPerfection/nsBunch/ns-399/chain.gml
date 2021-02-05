graph [
  node [
    id 0
    label 1
    disk 9
    cpu 4
    memory 14
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 2
    memory 7
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 1
    memory 9
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 3
    memory 1
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 10
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 4
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
    bw 62
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 190
  ]
  edge [
    source 1
    target 2
    delay 29
    bw 168
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 138
  ]
  edge [
    source 2
    target 4
    delay 27
    bw 189
  ]
  edge [
    source 3
    target 5
    delay 25
    bw 119
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 130
  ]
]
